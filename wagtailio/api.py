from django.shortcuts import get_object_or_404
from rest_framework.filters import BaseFilterBackend

from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.core.models import Locale, Page
from wagtail.api.v2.views import (
    AncestorOfFilter,
    ChildOfFilter,
    DescendantOfFilter,
    FieldsFilter,
    OrderingFilter,
    SearchFilter,
    TranslationOfFilter,
)

from wagtailio.areweheadlessyet.models import AreWeHeadlessYetHomePage

api_router = WagtailAPIRouter("wagtailapi")


class LocalesFilter(BaseFilterBackend):
    """
    Overrides the ?locale filter to limit the set of pages to a
    list of supported locales.
    """

    def filter_queryset(self, request, queryset, view):
        if "locale" in request.GET:
            _filtered_by_child_of = getattr(queryset, "_filtered_by_child_of", None)
            locales = []
            for locale_code in request.GET["locale"].split(','):
                locale = get_object_or_404(Locale, language_code=locale_code)
                locales += [locale]
            # print(f"locales: {locales}")
            queryset = queryset.filter(locale__in=locales)
            # print(f"queryset: {queryset}")

            if _filtered_by_child_of:
                queryset._filtered_by_child_of = _filtered_by_child_of

        return queryset


class AreWeHeadlessYetPagesAPIViewSet(PagesAPIViewSet):
    filter_backends = [
        FieldsFilter,
        ChildOfFilter,
        AncestorOfFilter,
        DescendantOfFilter,
        OrderingFilter,
        TranslationOfFilter,
        LocalesFilter, # swapping out LocaleFilter
        SearchFilter,
    ]


    def get_base_queryset(self):
        """Returns a queryset containing only pages from the AreWeHeadLessYet site."""

        pages = Page.objects.none()

        for root_page in AreWeHeadlessYetHomePage.objects.all():
            pages |= Page.objects.live().descendant_of(root_page, inclusive=True)

        return pages


api_router.register_endpoint("pages", AreWeHeadlessYetPagesAPIViewSet)
