## Bing Image Downloader 사용법
<hr>

### 설치하기 <br />
```sh
pip install bing-image-downloader
```

or 
```bash
git clone https://github.com/gurugaurav/bing_image_downloader
cd bing_image_downloader
pip install .
```


### 사용법 <br />
```python
from bing_image_downloader import downloader 

query_string = '진돗개'
downloader.download(query_string, limit=100,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
```

`query_string` : 검색어<br />
`limit` : (optional, default is 100) 다운로드할 최대 갯수<br />
`output_dir` : (optional, default is 'dataset') 파일 저장 폴더 이름, 기본 dataset.<br />
`adult_filter_off` : (optional, default is True) 성인용 여부<br />
`force_replace` : (optional, default is False) 저장 폴더가 존재할 경우 덮어쓰기 <br />
`timeout` : (optional, default is 60) 타임아웃<br />
`filter` : (optional, default is "") filter 종류 [line, photo, clipart, gif, transparent]<br />
`verbose` : (optional, default is True) Enable downloaded message.<br />



