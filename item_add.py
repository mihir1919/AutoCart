from selenium import webdriver
from time import sleep
import requests # to get image from the web
import shutil # to save it locally
import json
import os
js = [
  {
    "company": "Pyramis",
    "index": 0,
    "balance": 404283,
    "picture": "http://placehold.it/32x32",
    "city": "Ronco",
    "state": "North Dakota",
    "about": "Reprehenderit amet sunt Lorem nulla nisi. Consectetur magna eu non duis pariatur eu magna non pariatur dolore qui sit. Irure do labore ea veniam culpa qui occaecat culpa ullamco qui. Labore officia duis labore amet adipisicing nisi. Ipsum pariatur ullamco ex Lorem eu ea nostrud do enim cupidatat enim.\r\n"
  },
  {
    "company": "Netropic",
    "index": 1,
    "balance": 171897,
    "picture": "http://placehold.it/32x32",
    "city": "Libertytown",
    "state": "Palau",
    "about": "Pariatur adipisicing voluptate nostrud adipisicing duis eu do. Incididunt pariatur cupidatat in enim esse cupidatat exercitation irure sunt ad do magna. Reprehenderit deserunt duis aliquip ut laboris fugiat eiusmod esse elit officia do qui consectetur. Sit ad duis irure tempor irure eiusmod.\r\n"
  },
  {
    "company": "Synkgen",
    "index": 2,
    "balance": 305569,
    "picture": "http://placehold.it/32x32",
    "city": "Richmond",
    "state": "Virgin Islands",
    "about": "Ullamco amet ullamco minim cillum reprehenderit elit do. Ad dolore commodo aliqua culpa nulla mollit dolore voluptate nisi sunt culpa ex. Nulla irure Lorem pariatur elit qui non voluptate ex ullamco irure duis ex occaecat. Ipsum reprehenderit amet nostrud labore aliquip in est. Dolore elit ea consequat pariatur irure adipisicing quis aliqua ad labore consectetur elit. Sit voluptate ea ea est velit irure anim dolore Lorem ad dolor. In Lorem qui eiusmod anim ex voluptate esse elit deserunt.\r\n"
  },
  {
    "company": "Portaline",
    "index": 3,
    "balance": 377069,
    "picture": "http://placehold.it/32x32",
    "city": "Gilmore",
    "state": "Alaska",
    "about": "In fugiat culpa cillum proident dolor officia. Ipsum adipisicing ullamco nulla dolore. Est veniam sit duis anim est adipisicing culpa sunt irure nisi sit commodo tempor. Reprehenderit labore dolore non dolor sit aute tempor veniam amet deserunt nisi in aliquip. Incididunt dolor tempor velit eu tempor irure eiusmod exercitation quis et eiusmod quis consectetur.\r\n"
  },
  {
    "company": "Vendblend",
    "index": 4,
    "balance": 155014,
    "picture": "http://placehold.it/32x32",
    "city": "Lydia",
    "state": "Wisconsin",
    "about": "Laborum in Lorem cillum duis id consequat magna commodo est aliqua ut in. Amet ullamco magna cillum ex esse anim proident reprehenderit anim in aute minim veniam proident. Amet dolore voluptate magna tempor Lorem sint amet elit irure commodo. Exercitation dolor irure esse minim labore. Duis culpa reprehenderit reprehenderit labore aliquip Lorem aute cillum anim officia proident elit. Irure sint laboris do aliqua pariatur nisi exercitation ipsum culpa sunt cillum velit cillum. Incididunt irure anim occaecat voluptate.\r\n"
  },
  {
    "company": "Qualitern",
    "index": 5,
    "balance": 293443,
    "picture": "http://placehold.it/32x32",
    "city": "Makena",
    "state": "Texas",
    "about": "Cupidatat sunt tempor qui nostrud est enim. Irure dolore excepteur tempor deserunt ut occaecat laborum ullamco. Occaecat aliquip ad Lorem labore nostrud id aute dolore. Ullamco laboris sunt minim laboris aute. Cupidatat velit officia sit laborum aliqua esse in pariatur. Pariatur irure minim aute in proident sint Lorem adipisicing fugiat minim exercitation non.\r\n"
  },
  {
    "company": "Gonkle",
    "index": 6,
    "balance": 221894,
    "picture": "http://placehold.it/32x32",
    "city": "Westmoreland",
    "state": "North Carolina",
    "about": "Excepteur cupidatat voluptate est labore sint ea sint commodo cupidatat consectetur ut. Enim duis ut magna in qui voluptate non esse dolor dolore veniam cupidatat eiusmod tempor. Elit mollit fugiat nostrud Lorem qui ea occaecat nulla exercitation magna in enim. Aliqua quis nisi laboris dolor nostrud ad veniam minim. Do officia tempor occaecat enim Lorem ullamco commodo in laborum nisi laboris non reprehenderit. Incididunt dolore duis in occaecat voluptate tempor duis amet consectetur fugiat. Quis cupidatat proident duis irure eu dolor officia nisi est id eiusmod tempor.\r\n"
  },
  {
    "company": "Miraclis",
    "index": 7,
    "balance": 255626,
    "picture": "http://placehold.it/32x32",
    "city": "Harborton",
    "state": "Maine",
    "about": "Culpa laboris aliqua voluptate deserunt aliqua ex occaecat laborum proident duis laboris. Labore aute elit anim nulla dolor dolore aliqua Lorem Lorem mollit consectetur reprehenderit nostrud incididunt. Est nisi pariatur nostrud ipsum laborum ex labore consequat ut irure.\r\n"
  },
  {
    "company": "Greeker",
    "index": 8,
    "balance": 45980,
    "picture": "http://placehold.it/32x32",
    "city": "Edinburg",
    "state": "New Mexico",
    "about": "Pariatur sunt laborum proident sunt. Elit amet minim anim ad ut incididunt laborum. Sint est reprehenderit aliquip magna sint commodo ex reprehenderit qui ea laboris sunt est. Velit excepteur fugiat ut veniam et.\r\n"
  },
  {
    "company": "Duflex",
    "index": 9,
    "balance": 186492,
    "picture": "http://placehold.it/32x32",
    "city": "Cassel",
    "state": "Pennsylvania",
    "about": "Mollit culpa esse proident ipsum excepteur. Do id in enim deserunt laboris sunt. Quis do culpa velit aliquip incididunt sit amet officia aliqua dolore. Non ullamco dolore eiusmod magna nisi commodo eu ex. Nostrud sint duis irure ut.\r\n"
  },
  {
    "company": "Xerex",
    "index": 10,
    "balance": 68534,
    "picture": "http://placehold.it/32x32",
    "city": "Shelby",
    "state": "Idaho",
    "about": "Dolor cupidatat ea enim laboris commodo adipisicing tempor id. Et sint do laboris et sint adipisicing id cupidatat. Aliquip eu consectetur Lorem ipsum deserunt ut ad quis commodo minim nostrud occaecat. Quis aliquip ad qui enim eiusmod consequat ipsum. Amet commodo Lorem cupidatat non culpa sint sit qui pariatur.\r\n"
  },
  {
    "company": "Daisu",
    "index": 11,
    "balance": 344760,
    "picture": "http://placehold.it/32x32",
    "city": "Elizaville",
    "state": "Mississippi",
    "about": "Pariatur Lorem ullamco quis irure sit culpa tempor. Ad amet minim sint aliquip. Do ullamco fugiat cillum aute nostrud reprehenderit incididunt ipsum enim mollit duis.\r\n"
  },
  {
    "company": "Soprano",
    "index": 12,
    "balance": 65905,
    "picture": "http://placehold.it/32x32",
    "city": "Hall",
    "state": "Arizona",
    "about": "Occaecat nostrud culpa fugiat elit anim ipsum consectetur incididunt ad. Aliqua adipisicing consectetur nostrud ullamco. Aute ad irure tempor elit ea nostrud do cillum eu dolore sit esse do. Sint ipsum excepteur consequat laborum id elit. Cupidatat sunt magna sunt culpa voluptate exercitation ipsum amet culpa. Tempor nostrud Lorem deserunt pariatur in dolore ad irure incididunt. Aute esse incididunt nulla velit laborum occaecat fugiat velit aliqua.\r\n"
  },
  {
    "company": "Extragene",
    "index": 13,
    "balance": 339984,
    "picture": "http://placehold.it/32x32",
    "city": "Valle",
    "state": "Wyoming",
    "about": "Exercitation fugiat fugiat dolor proident dolore nulla aliquip ex amet minim irure anim mollit. Et nulla dolor mollit sit commodo sint exercitation eiusmod sunt cupidatat. Id cupidatat cupidatat minim velit aute culpa est ad elit mollit nulla aliquip elit Lorem. Aute nisi commodo labore laborum cupidatat amet cillum officia velit. Dolore ex magna anim cillum.\r\n"
  },
  {
    "company": "Pulze",
    "index": 14,
    "balance": 350896,
    "picture": "http://placehold.it/32x32",
    "city": "Tuttle",
    "state": "Minnesota",
    "about": "Ad tempor nostrud adipisicing eiusmod minim amet occaecat mollit et est reprehenderit. Est id laborum reprehenderit ullamco ut proident in aliqua aliquip esse. Ipsum incididunt Lorem voluptate exercitation amet nostrud Lorem consectetur. Amet aliquip mollit deserunt elit nisi consectetur. Aliquip ea nulla quis ullamco. Dolore pariatur laboris do labore consectetur adipisicing officia veniam reprehenderit cupidatat pariatur. Incididunt eu proident ullamco duis deserunt adipisicing aute amet non consectetur aliquip.\r\n"
  },
  {
    "company": "Assitia",
    "index": 15,
    "balance": 335124,
    "picture": "http://placehold.it/32x32",
    "city": "Selma",
    "state": "Rhode Island",
    "about": "Non non duis veniam eiusmod. Minim eiusmod eu mollit aute eu veniam sunt. Eu cillum esse elit minim duis. Aute aliqua nulla ex ullamco veniam officia Lorem nisi cillum sint dolore excepteur sit culpa. Reprehenderit aute eu anim Lorem. Aliquip eu est incididunt sunt. Adipisicing voluptate quis amet id velit pariatur est eu commodo laboris adipisicing qui Lorem.\r\n"
  },
  {
    "company": "Petigems",
    "index": 16,
    "balance": 85542,
    "picture": "http://placehold.it/32x32",
    "city": "Brogan",
    "state": "Michigan",
    "about": "Aliquip eu esse Lorem do tempor ullamco velit. Est ullamco eu eiusmod ex eiusmod mollit non fugiat et esse id ut. Anim velit nisi amet laboris ullamco cillum cillum ut nostrud. Non cupidatat tempor nisi do officia consequat elit sunt cillum eiusmod in mollit. Ipsum voluptate qui sint labore pariatur eiusmod.\r\n"
  },
  {
    "company": "Otherside",
    "index": 17,
    "balance": 429289,
    "picture": "http://placehold.it/32x32",
    "city": "Wedgewood",
    "state": "Massachusetts",
    "about": "Eiusmod esse mollit sint fugiat irure qui velit dolore sit commodo enim do labore. Id et proident voluptate ipsum pariatur nostrud. Laborum nulla consequat ea ipsum. Esse anim voluptate aliquip esse consequat proident culpa. Cupidatat ullamco Lorem ex eiusmod quis sunt. Aliquip sit elit consequat aliquip proident ex quis deserunt deserunt do occaecat deserunt pariatur.\r\n"
  },
  {
    "company": "Zerbina",
    "index": 18,
    "balance": 431960,
    "picture": "http://placehold.it/32x32",
    "city": "Jenkinsville",
    "state": "Nevada",
    "about": "Ea deserunt laboris esse aliquip reprehenderit ut occaecat nostrud sunt laboris laboris amet. Elit ea sint anim minim amet laborum laboris veniam amet consectetur irure proident labore velit. Esse reprehenderit labore deserunt commodo eu magna ut mollit sint. Eu sit et magna exercitation labore sit id nisi commodo ad sint. Nisi elit occaecat irure excepteur irure.\r\n"
  },
  {
    "company": "Zytrax",
    "index": 19,
    "balance": 74058,
    "picture": "http://placehold.it/32x32",
    "city": "Longoria",
    "state": "West Virginia",
    "about": "Aliquip excepteur magna irure et proident in sunt nostrud minim amet ad et cupidatat. Deserunt ipsum esse esse veniam commodo ullamco. Cupidatat quis consequat esse anim fugiat duis enim nisi cupidatat id ut nostrud eu.\r\n"
  }
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class add():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('http://mcraig.herokuapp.com/')

        sleep(2)
        
        fb_btn = bot.driver.find_element_by_xpath('/html/body/nav/div/ul/li[1]/a')
        fb_btn.click()

        name = self.driver.find_element_by_xpath('//*[@id="id_username"]')
        name.send_keys('mihir')

        password = self.driver.find_element_by_xpath('//*[@id="id_password"]')
        password.send_keys('barcelona19')
        
        login = bot.driver.find_element_by_xpath('/html/body/div/form/button')
        login.click()

        red = self.driver.find_element_by_xpath('/html/body/div/a/button')
        red.click()

        self.sell()
        # sel = self.driver.find_element_by_xpath('//*[@id="navcol-1"]/ul[1]/li[2]/a')
        # sel.click()

        # sname=self.driver.find_element_by_xpath('//*[@id="id_name"]')
        # sprice=self.driver.find_element_by_xpath('//*[@id="id_price"]')
        # sdec=self.driver.find_element_by_xpath('//*[@id="id_desc"]')
        # sstate=self.driver.find_element_by_xpath('//*[@id="id_state"]')
        # scity=self.driver.find_element_by_xpath('//*[@id="id_city"]')
        # simg=self.driver.find_element_by_xpath('//*[@id="id_img"]')
        # sauthor=self.driver.find_element_by_xpath('//*[@id="id_author"]')

        # d=js[0]
        # sname.send_keys(d['company'])
        # sprice.send_keys(d['balance'])
        # sdec.send_keys(d['about'])
        # sstate.send_keys(d['state'])
        # scity.send_keys(d['city'])
        # picture = requests.get("https://picsum.photos/500/600")
        # picture = picture.url
        # simg.send_keys(picture)
        # sauthor.send_keys('mihir')

    def sell(self):

        sel = self.driver.find_element_by_xpath('//*[@id="navcol-1"]/ul[1]/li[2]/a')
        sel.click()
        
        for i in range(len(js)):
          sleep(2)
          sname=self.driver.find_element_by_xpath('//*[@id="id_name"]')
          sprice=self.driver.find_element_by_xpath('//*[@id="id_price"]')
          sdec=self.driver.find_element_by_xpath('//*[@id="id_desc"]')
          sstate=self.driver.find_element_by_xpath('//*[@id="id_state"]')
          scity=self.driver.find_element_by_xpath('//*[@id="id_city"]')
          simg=self.driver.find_element_by_xpath('//*[@id="id_img"]')
          sauthor=self.driver.find_element_by_xpath('//*[@id="id_author"]')   
          d=js[i]
          sleep(2)
          sname.send_keys(d['company'])
          sprice.send_keys(d['balance'])
          sdec.send_keys(d['about'])
          sstate.send_keys(d['state'])
          scity.send_keys(d['city'])
          picture = requests.get("https://picsum.photos/500/600")
          picture = picture.url
          simg.send_keys(picture)
          sauthor.send_keys('mihir')
          sleep(0.3)
          btn=self.driver.find_element_by_xpath('/html/body/div[1]/form/button')
          btn.click()
          sleep(1)
          sel = self.driver.find_element_by_xpath('//*[@id="navcol-1"]/ul[1]/li[2]/a')
          sel.click()
          sleep(1)