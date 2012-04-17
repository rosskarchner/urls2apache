from django.conf import settings
from django.core.management.base import NoArgsCommand


def url_pattern_to_apache(pattern, parent=None):
    if parent:
        print parent.regex.pattern + pattern.regex.pattern
    else:
        print pattern.regex.pattern
    if hasattr(pattern, 'url_patterns'):
        for sub_pattern in pattern.url_patterns:
            url_pattern_to_apache(sub_pattern, parent=pattern)



class Command(NoArgsCommand):
     def handle(self, **options):
        url_root=__import__(settings.ROOT_URLCONF)
        for pattern in url_root.urlpatterns:
            url_pattern_to_apache(pattern)