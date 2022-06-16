from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.core.models import Page

from wagtailio.areweheadlessyet.models import AreWeHeadlessYetHomePage

api_router = WagtailAPIRouter("wagtailapi")


class AreWeHeadlessYetPagesAPIViewSet(PagesAPIViewSet):
    def get_base_queryset(self):
        """Returns a queryset containing only pages from the AreWeHeadLessYet site."""

        pages = Page.objects.none()

        for root_page in AreWeHeadlessYetHomePage.objects.all():
            pages |= Page.objects.live().descendant_of(
                root_page, inclusive=True
            )

        return pages


api_router.register_endpoint("pages", AreWeHeadlessYetPagesAPIViewSet)
