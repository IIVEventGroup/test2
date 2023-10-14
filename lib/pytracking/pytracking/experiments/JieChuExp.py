from pytracking.evaluation import Tracker, get_dataset, trackerlist, load_stream_setting


trackers4improve1st =  trackerlist('atom', 'default',range(5)) + \
            trackerlist('atom', 'fe240',range(5)) + \
            trackerlist('dimp', 'dimp18',range(5)) + \
            trackerlist('dimp', 'dimp18_fe240',range(5)) +\
            trackerlist('dimp', 'prdimp18',range(5)) +\
            trackerlist('dimp', 'dimp50',range(5)) + \
            trackerlist('kys', 'default',range(5)) + \
            trackerlist('kys', 'fe240',range(5)) + \
            trackerlist('rts','rts50',range(5)) + \
            trackerlist('keep_track','default',range(5)) + \
            trackerlist('tomp','tomp50',range(5))

trackers_transferd_JieChu_esot500 =  trackerlist('dimp', 'JieChu_dimp50_esot500') + \
            trackerlist('tomp', 'JieChu_tomp50_esot500') 
            # trackerlist('keeptrack', 'JieChu_esot500')
            # trackerlist('tomp', 'JieChu_tomp101_esot500')

allTrackers_esot500 = trackerlist('atom', 'esot500') + \
            trackerlist('dimp', 'dimp18_esot500') + \
            trackerlist('dimp', 'JieChu_dimp50_esot500') + \
            trackerlist('prdimp', 'prdimp18_esot500') + \
            trackerlist('prdimp', 'prdimp50_esot500') + \
            trackerlist('keeptrack', 'JieChu_esot500') + \
            trackerlist('kys', 'esot500') + \
            trackerlist('lwl', 'esot500') + \
            trackerlist('tomp', 'JieChu_tomp50_esot500') + \
            trackerlist('tomp', 'JieChu_tomp101_esot500')


allTrackers_fe240 = trackerlist('atom', 'fe240') + \
            trackerlist('dimp', 'dimp18_fe240') + \
            trackerlist('dimp', 'JieChu_dimp50_fe240') + \
            trackerlist('prdimp', 'prdimp18_fe240') + \
            trackerlist('prdimp', 'prdimp50_fe240') + \
            trackerlist('kys', 'fe240') + \
            trackerlist('lwl', 'fe240') + \
            trackerlist('tomp', 'tomp50_fe240') + \
            trackerlist('tomp', 'JieChu_tomp101_fe240')


allTrackers_default = trackerlist('atom', 'default') + \
            trackerlist('dimp', 'dimp18') + \
            trackerlist('dimp', 'dimp50') + \
            trackerlist('prdimp', 'prdimp18') + \
            trackerlist('prdimp', 'prdimp50') + \
            trackerlist('keeptrack', 'default') + \
            trackerlist('kys', 'default') + \
            trackerlist('lwl', 'default') + \
            trackerlist('tomp', 'tomp50') + \
            trackerlist('tomp', 'tomp101')

def streaming_trackers4improve1st():
    trackers =  trackers_single_5range
    # dataset = get_dataset('esot500s','esot2s')
    dataset = get_dataset('esot500s')
    stream_setting = load_stream_setting('s31')
    return trackers, dataset, stream_setting

def streaming_transferd_JieChu_esot500():
    trackers=trackers_transferd_JieChu_esot500
    dataset=get_dataset('esot500s')
    stream_setting = load_stream_setting('s15')
    return trackers, dataset, stream_setting