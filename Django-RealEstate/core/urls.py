from django.urls import path

from .views import (IndexView, AboutView, ContactView, ImpressumView, PrivacyView, policyView, termsView, Gallaryview,
                    RobotsTXTView)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('robots.txt', RobotsTXTView.as_view(content_type="text/plain")),
    path('contact-us', ContactView.as_view(), name='contact'),
    path('about-us', AboutView.as_view(), name='about'),
    path('impressum', ImpressumView.as_view(), name="impressum"),
    path('privacy', PrivacyView.as_view(), name="privacy"),
    path('policy', policyView.as_view(), name="policy"),
    path('terms', termsView.as_view(), name="terms"),
    path('gallary', Gallaryview.as_view(), name="gallary"),

]
