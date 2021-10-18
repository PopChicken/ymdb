from django_hosts import patterns, host


host_patterns = patterns('',
    host(r'ymdb', 'ymdb_web.urls', name='web'),
    host(r'127.0.0.1:8000', 'ymdb.urls', name='ymdb'),
)