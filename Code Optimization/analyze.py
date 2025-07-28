import pstats

stats = pstats.Stats('profile.prof')
stats.print_stats()
