from bing_image_downloader import downloader

query_string = "진돗개"
downloader.download(query_string, 
                    limit=10,  
                    output_dir='dataset', 
                    adult_filter_off=True, 
                    force_replace=False, 
                    timeout=60, verbose=True)

