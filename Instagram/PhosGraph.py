# parse Instagram page html
soup = BeautifulSoup(driver.page_source, "html.parser")

# create json
j = {}
j['followers'] = soup.find_all('span', {'class' : 'g47SY'})[1]['title']
j['ig']=driver.current_url

# save json in PhosGraph database
driver.get("http://phos.epizy.com/phos/post_rc.php?r=&c=")
u_j=driver.find_element_by_xpath('//*[@id="json"]')
u_j.send_keys(json.dumps(j))
u_s=driver.find_element_by_xpath('/html/body/form/input[3]')
u_s.click()

# move back to Instagram page
driver.get(j['ig'])

