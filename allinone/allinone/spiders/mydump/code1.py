import urll_proxy
from bs4 import BeautifulSoup


def main():
    link = "http://www.flipkart.com/"
    
    page = urll_proxy.main(link)
    soup = BeautifulSoup(page.read())
    page.close()

    tag_menu = soup.find_all("li", attrs={"class":"menu-l0"})

    dict_menu_link = {}

    for l in tag_menu:
        menu = str(l.get("data-key")).strip()
        tag_menu_item = l.find_all("li", attrs={"class":"menu-item"})

	dict_menu_link[menu] = []
        
	for l in tag_menu_item:
	    try:
	        full_link = "http://www.flipkart.com" + l.a.get("href")
	        dict_menu_link[menu].append(full_link)
	    
	    except:
	        pass
     
    f = open("code1_dict_menu_link.txt", "w+")
    print >>f, dict_menu_link
    f.close()


        

if __name__=="__main__":
    main()
