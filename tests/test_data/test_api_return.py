"""holds classes for testing the API functions with fake information"""
from models.exceptions import *

class TestingEventApi:
    """used to get fake test data"""
    @staticmethod
    def verify_request_is_correct(requestData):
        """verifies the request is in the correct format"""
        requiredAttrs = ["place_address",
                         "place_latitude",
                         "place_longitude",
                         "selected_date_event_api",
                         "selected_days_weather_api"]
        for attr in requiredAttrs:
            if attr not in requestData.keys():
                raise TestRequestDataIncorrectFormat

test_return_dto = {"eventList": [
        {
            "title": "Avi Avital",
            "date": {
                "start_date": "Sep 24",
                "when": "Sat, Sep 24, 7 – 9 PM GMT+10"
            },
            "address": [
                "Melbourne Recital Centre, 31 Sturt St",
                "Southbank VIC, Australia"
            ],
            "link": "https://www.songkick.com/concerts/40429762-avi-avital-at-melbourne-recital-centre?utm_medium=organic&utm_source=microformat",
            "event_location_map": {
                "image": "https://www.google.com/maps/vt/data=2ikm3IrGV_2-ngdl3aatgFd0wRGHiRMlLfTnQSvphlNMH3xazkPtQ4KUzD4sHbI4oOtbXkhHtjTVyEEbdIJVdAUkIpLLwqoI4DzZf5gzszkeaJt8MPE",
                "link": "https://www.google.com/maps/place//data=!4m2!3m1!1s0x6ad642ae1a5e9b83:0xef21a57877623bbe?sa=X&hl=en",
                "serpapi_link": "https://serpapi.com/search.json?data=%214m2%213m1%211s0x6ad642ae1a5e9b83%3A0xef21a57877623bbe&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Melbourne%2C+Vic+on+24%2F09%2F2022&type=place"
            },
            "description": "Avi Avital and Giovanni Sollima at Melbourne Recital Centre at 2022-09-24",
            "ticket_info": [
                {
                    "source": "Songkick.com",
                    "link": "https://www.songkick.com/concerts/40429762-avi-avital-at-melbourne-recital-centre?utm_medium=organic&utm_source=microformat",
                    "link_type": "tickets"
                },
                {
                    "source": "Limelight Magazine",
                    "link": "https://limelightmagazine.com.au/event/avi-avital-giovanni-sollima-4/2022-09-24/",
                    "link_type": "more info"
                },
                {
                    "source": "Continuo Community",
                    "link": "https://continuo.org.au/event/avital-sollima-scarlatti-sollima-castello-frescobaldi-traditional/2022-09-24/",
                    "link_type": "more info"
                },
                {
                    "source": "My Community Diary",
                    "link": "https://www.mycommunitydiary.com.au/Victoria/Melbourne/Avi_Avital_and_Giovanni_Sollima/175041/3055412",
                    "link_type": "more info"
                },
                {
                    "source": "Common Times",
                    "link": "https://commontimes.com.au/events/avi-avital-and-giovanni-sollima-39103",
                    "link_type": "more info"
                }
            ],
            "venue": {
                "name": "Melbourne Recital Centre",
                "rating": 4.8,
                "reviews": 1184,
                "link": "https://www.google.com/search?hl=en&q=Melbourne+Recital+Centre&ludocid=17231235586113813438&ibp=gwp%3B0,7"
            },
            "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSu7fMd__5u6xhglIF3IEZW-E5G9ePFSCBMK90qlOkD0K4dSbSS2Sn6Ve0&s",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyv2akIbFVKQ436gGwt-NJuojN8gmv9G8yD5sss_HzTCT6JZlxJnPrtPgrUQ&s=10"
        },
        {
            "title": "Xe54 - 24/09/22",
            "date": {
                "start_date": "Sep 24",
                "when": "Sat, Sep 24 – Sun, Sep 25"
            },
            "address": [
                "Xe54, 579 Little Collins St",
                "Melbourne VIC, Australia"
            ],
            "link": "https://allevents.in/melbourne/xe54-24-09-22/10000394187374047",
            "event_location_map": {
                "image": "https://www.google.com/maps/vt/data=2cmb35aDxW9jOp6KM7F24oXR7yTuV3_8o9GW6Y8AIgjog63KDG-K_MFOdzhxTJs7wXHCDzoyfVu9mjzA75OfYvGOVn1ddG1bQqBi7GOBkY7t_nAedq4",
                "link": "https://www.google.com/maps/place//data=!4m2!3m1!1s0x6ad65d55b9504617:0x947c214ba9985b00?sa=X&hl=en",
                "serpapi_link": "https://serpapi.com/search.json?data=%214m2%213m1%211s0x6ad65d55b9504617%3A0x947c214ba9985b00&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Melbourne%2C+Vic+on+24%2F09%2F2022&type=place"
            },
            "ticket_info": [
                {
                    "source": "Eventbrite.com.au",
                    "link": "https://www.eventbrite.com.au/e/xe54-240922-tickets-394187374047",
                    "link_type": "tickets"
                },
                {
                    "source": "AllEvents.in",
                    "link": "https://allevents.in/melbourne/xe54-24-09-22/10000394187374047",
                    "link_type": "more info"
                }
            ],
            "venue": {
                "name": "Xe54",
                "rating": 3.2,
                "reviews": 66,
                "link": "https://www.google.com/search?hl=en&q=Xe54&ludocid=10699463423577053952&ibp=gwp%3B0,7"
            },
            "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzSNeuEusxLtlFpO3bTu1gkpH1gSUa7Y6FuPPmCMxjCuphFPFj6UJDkXs&s",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTv8ksjgcOImor7wz9VvDQbsHM7u4Z54AA7SioCDTpuwbyJ21NxT6URkypnbw&s=10"
        },
        {
            "title": "Main Stage @ Comedy Republic",
            "date": {
                "start_date": "Sep 24",
                "when": "Sat, 8:30 – 10:00 PM"
            },
            "address": [
                "Comedy Republic, 231 Bourke St",
                "Melbourne VIC, Australia"
            ],
            "link": "https://www.eventbrite.com.au/e/main-stage-comedy-with-harry-jun-prue-blake-more-tickets-368750993147",
            "event_location_map": {
                "image": "https://www.google.com/maps/vt/data=wIqWsp1-GGcNcCG9pcdLjM59HuZ4uRl54WfMXpwe5hDeZXlaD59rkC2ana1kq0chd-pQ_u-HXQac7-LihJazvkXFtLhVdLzSxLjisvn5-Vmptzt70D4",
                "link": "https://www.google.com/maps/place//data=!4m2!3m1!1s0x6ad643f87996e99b:0xa4e5b67e456665b4?sa=X&hl=en",
                "serpapi_link": "https://serpapi.com/search.json?data=%214m2%213m1%211s0x6ad643f87996e99b%3A0xa4e5b67e456665b4&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Melbourne%2C+Vic+on+24%2F09%2F2022&type=place"
            },
            "description": "Prue Blake, Harry Jun, Lou Wall, Ben Searle, Rohan Ganju & More",
            "ticket_info": [
                {
                    "source": "Eventbrite.com.au",
                    "link": "https://www.eventbrite.com.au/e/main-stage-comedy-with-harry-jun-prue-blake-more-tickets-368750993147",
                    "link_type": "tickets"
                },
                {
                    "source": "Tixel.com",
                    "link": "https://tixel.com/au/comedy-tickets/2022/09/24/main-stage",
                    "link_type": "tickets"
                },
                {
                    "source": "Beat Magazine",
                    "link": "https://beat.com.au/main-stage-comedy-republic-13/",
                    "link_type": "more info"
                },
                {
                    "source": "AllEvents.in",
                    "link": "https://allevents.in/melbourne/main-stage-comedy-saturday-24-september-7pm/10000368750993147",
                    "link_type": "more info"
                }
            ],
            "venue": {
                "name": "Comedy Republic",
                "rating": 4.7,
                "reviews": 164,
                "link": "https://www.google.com/search?hl=en&q=Comedy+Republic&ludocid=11882103845333394868&ibp=gwp%3B0,7"
            },
            "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRy-JcoSY_bQyn_nPzIKinKUSdJSkdMbg6iv3Cqwv1WAcfXJs3lfg1Rw6s&s",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSi57_2UOkSqO3jnfmsK5tqqliMkZ0f5KXnwT5KxSsNbw&s=10"
        },
        {
            "title": "Cocktails & Techno - September 24th",
            "date": {
                "start_date": "Sep 24",
                "when": "Sat, 4 – 10 PM"
            },
            "address": [
                "Circus Bar, 199 Commercial Rd",
                "South Yarra VIC, Australia"
            ],
            "link": "https://allevents.in/mobile/amp-event.php?event_id=10000382715060047",
            "event_location_map": {
                "image": "https://www.google.com/maps/vt/data=S3AYnKujvhgGenWTEZv4zMcEHWtby8Vs7P81GW1yurGoXkY-4_zgcA1DR04EbSyOSM07mC8BslhxV4UHJSDLuPIYEw_-p8wNJqiIaVwdDrn1yDCqlNw",
                "link": "https://www.google.com/maps/place//data=!4m2!3m1!1s0x6ad66825ef36ba17:0xe57204a3867729c4?sa=X&hl=en",
                "serpapi_link": "https://serpapi.com/search.json?data=%214m2%213m1%211s0x6ad66825ef36ba17%3A0xe57204a3867729c4&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Melbourne%2C+Vic+on+24%2F09%2F2022&type=place"
            },
            "ticket_info": [
                {
                    "source": "AllEvents.in",
                    "link": "https://allevents.in/mobile/amp-event.php?event_id=10000382715060047",
                    "link_type": "more info"
                }
            ],
            "venue": {
                "name": "Circus Bar",
                "rating": 3.7,
                "reviews": 260,
                "link": "https://www.google.com/search?hl=en&q=Circus+Bar&ludocid=16533282282412648900&ibp=gwp%3B0,7"
            },
            "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToFUyKxQhUPQTEBoZc8Rlw9-brUjgT1pKDgTdaJfvZnDfiMjErdZSnhJPX2g&s"
        },
        {
            "title": "Exclusive Screenings 'Wog Boys Forever' with Nick...",
            "date": {
                "start_date": "Sep 24",
                "when": "Sat, Sep 24 – Sun, Sep 25"
            },
            "address": [
                "Palais Theatre., Lower Esplanade",
                "St Kilda VIC, Australia"
            ],
            "link": "https://www.ticketmaster.com.au/exclusive-screenings-wog-boys-forever-with-nick-giannopoulos-live-st-kilda-24-09-2022/event/13005CBF894616EE",
            "event_location_map": {
                "image": "https://www.google.com/maps/vt/data=ydV55Y6g5RW_8LZ5c2IMElNvEyoc9yYDckem6zIBa2hkWs10vlg0JMWgUqlXvwFV0eW0WXCEtzbnWByHupfpGF4VVl9hDJKC6MpoFKkBOuBDoW75ZGM",
                "link": "https://www.google.com/maps/place//data=!4m2!3m1!1s0x6ad668646ab8aae7:0xc8221ae7bcc188e4?sa=X&hl=en",
                "serpapi_link": "https://serpapi.com/search.json?data=%214m2%213m1%211s0x6ad668646ab8aae7%3A0xc8221ae7bcc188e4&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Melbourne%2C+Vic+on+24%2F09%2F2022&type=place"
            },
            "description": "Tickets: for Exclusive Screenings 'Wog Boys Forever' with Nick Giannopoulos Live! @ Palais Theatre | Sat, 24 Sept 2022, 8:00 pm | Browse ticket types & offers | View seating map",
            "ticket_info": [
                {
                    "source": "Tixel.com",
                    "link": "https://tixel.com/au/comedy-tickets/2022/09/24/exclusive-screenings-wog-boys-fo",
                    "link_type": "tickets"
                },
                {
                    "source": "Theatresonline.com.au",
                    "link": "https://www.theatresonline.com.au/shows/palais-theatre/exclusive-screenings-wog-boys-forever-with-nick-giannopoulos-live",
                    "link_type": "tickets"
                },
                {
                    "source": "Tm7566.net",
                    "link": "https://ticketmaster-au.tm7566.net/c/253520/431533/7566?u=https%3A%2F%2Fwww.ticketmaster.com.au%2Fexclusive-screenings-wog-boys-forever-with-st-kilda-victoria-09-24-2022%2Fevent%2F13005CBF894616EE",
                    "link_type": "tickets"
                },
                {
                    "source": "Ticketmaster",
                    "link": "https://www.ticketmaster.com.au/exclusive-screenings-wog-boys-forever-with-nick-giannopoulos-live-st-kilda-24-09-2022/event/13005CBF894616EE",
                    "link_type": "more info"
                },
                {
                    "source": "AllEvents.in",
                    "link": "https://allevents.in/melbourne/exclusive-screenings-wog-boys-forever-with-nick-giannopoulos-live/200023060556724",
                    "link_type": "more info"
                }
            ],
            "venue": {
                "name": "Palais Theatre.",
                "rating": 4.5,
                "reviews": 2679,
                "link": "https://www.google.com/search?hl=en&q=Palais+Theatre.&ludocid=14421118539400317156&ibp=gwp%3B0,7"
            },
            "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmoN1JwucElpJdIfDGDgL88cVHny_bBofocyH96nRIjBqBf5Bi6yis6Mg&s",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToFUyKxQhUPQTEBoZc8Rlw9-brUjgT1pKDgTdaJfvZnDfiMjErdZSnhJPX2g&s"
        },
        {
            "title": "Kings of Comedy's Melbourne Showcase Special",
            "date": {
                "start_date": "Sep 24",
                "when": "Sat, 7:00 – 8:30 PM"
            },
            "address": [
                "The Colonial Hotel, 585 Lonsdale St",
                "Melbourne VIC, Australia"
            ],
            "link": "https://www.eventbrite.com.au/e/kings-of-comedys-melbourne-showcase-special-tickets-349295190317",
            "event_location_map": {
                "image": "https://www.google.com/maps/vt/data=_rMvF6kNenuJYlrijBlrEI0MnOWqnheGhjmr2y8-bKt8vjPWqY1mlKNIzMHtX0bPVm55NOOn0t5EAp7p70m8SdLZ7d5KW4TR4xmkYZtbJWnkk9XxuyM",
                "link": "https://www.google.com/maps/place//data=!4m2!3m1!1s0x6ad6ecc832a92b73:0xc52269d36fb50ea?sa=X&hl=en",
                "serpapi_link": "https://serpapi.com/search.json?data=%214m2%213m1%211s0x6ad6ecc832a92b73%3A0xc52269d36fb50ea&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Melbourne%2C+Vic+on+24%2F09%2F2022&type=place"
            },
            "description": "Kings of Comedy's crusade returns with our popular showcase. Come enjoy some gut busting laughs and let's make date night great again.",
            "ticket_info": [
                {
                    "source": "Eventbrite.com.au",
                    "link": "https://www.eventbrite.com.au/e/kings-of-comedys-melbourne-showcase-special-tickets-191936054907",
                    "link_type": "tickets"
                },
                {
                    "source": "Tixel.com",
                    "link": "https://tixel.com/au/comedy-tickets/2022/09/24/kings-of-comedy-s-melbourne-show",
                    "link_type": "tickets"
                }
            ],
            "venue": {
                "name": "The Colonial Hotel",
                "rating": 3.8,
                "reviews": 295,
                "link": "https://www.google.com/search?hl=en&q=The+Colonial+Hotel&ludocid=887814533219569898&ibp=gwp%3B0,7"
            },
            "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcJ_MHSvkCuZCJQPRcez5AVBEvgr4Hm4lZmyKIMEVaypDvAZNahkCOL_E&s",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyK9DC-SK1h41kcYQf3yUvxpRIWjT08P9WAh6xNjkZ_o9cR9jW6_iroUgHZQ&s"
        },
        {
            "title": "Best of the Comedy Festival",
            "date": {
                "start_date": "Sep 23",
                "when": "Fri, Sep 23 – Sat, Sep 24"
            },
            "address": [
                "The Comic's Lounge, 1/26 Errol St",
                "North Melbourne VIC, Australia"
            ],
            "link": "https://tixel.com/au/comedy-tickets/2022/09/23/best-of-the-comedy-festival",
            "event_location_map": {
                "image": "https://www.google.com/maps/vt/data=xbXXAaVwLQo07Qg5cZU27HulY10X9kfknli7aoc563N4gvx1fsLH5yFzd1ujROVDZ4tJbm26tdlh2Kq6JQgwL70AS7KSXt1xVaZhYrNiAJz21B1lej4",
                "link": "https://www.google.com/maps/place//data=!4m2!3m1!1s0x6ad65d39de06dfd1:0xa599834c6e8596f1?sa=X&hl=en",
                "serpapi_link": "https://serpapi.com/search.json?data=%214m2%213m1%211s0x6ad65d39de06dfd1%3A0xa599834c6e8596f1&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Melbourne%2C+Vic+on+24%2F09%2F2022&type=place"
            },
            "ticket_info": [
                {
                    "source": "Tixel.com",
                    "link": "https://tixel.com/au/comedy-tickets/2022/09/23/best-of-the-comedy-festival",
                    "link_type": "tickets"
                },
                {
                    "source": "Tm7566.net",
                    "link": "https://ticketmaster-au.tm7566.net/c/253520/431533/7566?u=https%3A%2F%2Fwww.ticketmaster.com.au%2Fbest-of-the-comedy-festival-north-melbourne-victoria-09-23-2022%2Fevent%2F13005D21136C6965",
                    "link_type": "tickets"
                }
            ],
            "venue": {
                "name": "The Comic's Lounge",
                "rating": 4.6,
                "reviews": 2168,
                "link": "https://www.google.com/search?hl=en&q=The+Comic%27s+Lounge&ludocid=11932713051989841649&ibp=gwp%3B0,7"
            },
            "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzE_MyUnCExgDZSeZMSZppenYOS8Sf68iyNHqHE27mNJ80_oKjGcCiNbU&s",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIJR0xh2fKXYc8C90ioFiFbVgRz6AElKWihLEEliPBWg&s"
        },
        {
            "title": "Xclusive The Show | Melbourne",
            "date": {
                "start_date": "Sep 24",
                "when": "Sat, 6:30 – 10:00 PM"
            },
            "address": [
                "Wink Wink, 132 Greville St",
                "Prahran VIC, Australia"
            ],
            "link": "https://www.eventbrite.com.au/e/xclusive-the-show-melbourne-tickets-315233942207",
            "event_location_map": {
                "image": "https://www.google.com/maps/vt/data=L6MAAt2BV_1Rx_4mA8WuzkuJ4rXh45Rb_YeqCa0xDgJpisZORDILlLFtSnwvy2Qd-yLIExP2bWFuO2SAJByXzwh99v9GrKHtO5pxvoAujNjiFsQ2I2I",
                "link": "https://www.google.com/maps/place//data=!4m2!3m1!1s0x6ad66824d97edfe3:0x9cc3df87634c53a5?sa=X&hl=en",
                "serpapi_link": "https://serpapi.com/search.json?data=%214m2%213m1%211s0x6ad66824d97edfe3%3A0x9cc3df87634c53a5&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Melbourne%2C+Vic+on+24%2F09%2F2022&type=place"
            },
            "description": "Xclusive The Show - Melbourne's Finest Male Cabaret We welcome you to this lavish venue where you can celebrate your special occasion in classy atmosphere with an immersive cabaret experience...",
            "ticket_info": [
                {
                    "source": "Eventbrite.com.au",
                    "link": "https://www.eventbrite.com.au/e/xclusive-the-show-melbourne-tickets-315233942207",
                    "link_type": "tickets"
                },
                {
                    "source": "Tixel.com",
                    "link": "https://tixel.com/au/theatre-tickets/2022/09/24/xclusive-the-show-melbourne",
                    "link_type": "tickets"
                },
                {
                    "source": "AllEvents.in",
                    "link": "https://allevents.in/melbourne/theatre%20style",
                    "link_type": "more info"
                }
            ],
            "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRG3zdg9EMu77xt3cPST9pRDI2_LHKOxsulM-Ax_jrx2xnLv19527umnZU&s",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4UGn-jOAw2WnEskkK8frK0EiNw3pFe0vwwLrhmKjidQ&s=10"
        },
        {
            "title": "WILD BLOOMING | Spring Equinox — Love Bean Cacao",
            "date": {
                "start_date": "Sep 24",
                "when": "Sat, 3:00 – 4:45 PM"
            },
            "address": [
                "Centre of You, Upstairs, Nestled above Chapel St Bazaar, 217 Chapel St",
                "Prahran VIC, Australia"
            ],
            "link": "https://www.lovebeancacao.com.au/events/wild-blooming-spring-equinox",
            "event_location_map": {
                "image": "https://www.google.com/maps/vt/data=bvGpB3c-qHQ0Rwu2Bhij4lmvI3cMm-5TKA_LCe2z0mmECmDT_rMdoQX1932EaEqPvgaGpGVQmRPFLUqojMyi-FekjtQb6-h-XQvxKzUXPCfHo5YZIBM",
                "link": "https://www.google.com/maps/place//data=!4m2!3m1!1s0x6ad6683ab4c55555:0xb1f23c523ae2011e?sa=X&hl=en",
                "serpapi_link": "https://serpapi.com/search.json?data=%214m2%213m1%211s0x6ad6683ab4c55555%3A0xb1f23c523ae2011e&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Melbourne%2C+Vic+on+24%2F09%2F2022&type=place"
            },
            "description": "Honouring this ancient marker of seasonal change with the opportunity to bloom wildly working with the medicine of community, cacao, dance & ritual (and MORE!)",
            "ticket_info": [
                {
                    "source": "Allevents.in",
                    "link": "https://allevents.in/bazaar/wild-blooming-spring-equinox-cacao-dance-celebration/10000401869802397",
                    "link_type": "tickets"
                },
                {
                    "source": "Eventbrite.com",
                    "link": "https://www.eventbrite.com/e/wild-blooming-spring-equinox-cacao-dance-celebration-tickets-401869802397",
                    "link_type": "tickets"
                },
                {
                    "source": "Love Bean Cacao",
                    "link": "https://www.lovebeancacao.com.au/events/wild-blooming-spring-equinox",
                    "link_type": "more info"
                }
            ],
            "venue": {
                "name": "Centre of You",
                "rating": 5,
                "reviews": 5,
                "link": "https://www.google.com/search?hl=en&q=Centre+of+You&ludocid=12822377412950098206&ibp=gwp%3B0,7"
            },
            "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSNEsgsAR7PcOh-kCJ7Eq-45ym_D4fs0Av_JQHM9Jxt5QRJr12AfGFVftY&s",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSavXqISnffJGl2t583AyyztBza2RTV0GV63LzkdikmlETWwH-subiWHBHnFA&s"
        },
        {
            "title": "AFL Gran Final",
            "date": {
                "start_date": "Sep 24",
                "when": "Sat, 8 – 10 PM"
            },
            "address": [
                "Basement Comedy Club, Downstairs, 120 Exhibition St",
                "Melbourne VIC, Australia"
            ],
            "link": "https://www.eventbrite.com.au/e/grand-final-day-comedy-at-basement-comedy-club-saturday-september-24-8pm-tickets-413965300357",
            "event_location_map": {
                "image": "https://www.google.com/maps/vt/data=Qcl7xaAbpq_-HHFkTPasdEXmE0c3HIb2yJv3vHXEJTIs8xAb_QJ0UDYykqSH7Oe5vVyhI83_K3GvBQ2Ti0KMLCmehoUnfEH95qoNDOd_bekQzneWesE",
                "link": "https://www.google.com/maps/place//data=!4m2!3m1!1s0x6ad6436079ee8649:0x17d5fc8eb40fc1b7?sa=X&hl=en",
                "serpapi_link": "https://serpapi.com/search.json?data=%214m2%213m1%211s0x6ad6436079ee8649%3A0x17d5fc8eb40fc1b7&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Melbourne%2C+Vic+on+24%2F09%2F2022&type=place"
            },
            "description": "Ivan Aristeguieta hosts a big lineup at Basement Comedy Club on Saturday, on AFL Grand Final day! It's a big Melbourne night of comedy!",
            "ticket_info": [
                {
                    "source": "Eventbrite.com.au",
                    "link": "https://www.eventbrite.com.au/e/grand-final-day-comedy-at-basement-comedy-club-saturday-september-24-8pm-tickets-413965300357",
                    "link_type": "tickets"
                }
            ],
            "venue": {
                "name": "Basement Comedy Club",
                "rating": 4.8,
                "reviews": 4,
                "link": "https://www.google.com/search?hl=en&q=Basement+Comedy+Club&ludocid=1717556522748199351&ibp=gwp%3B0,7"
            },
            "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGtjpBeZWXkkVD_8DOtCNQsq4JMwxJqpUYPUYgSfQnA7YeJknRc7dRlu0&s",
            "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJHlimU6-mDoOuOFbq9Xq4MPSf8YwNKPuPBDlyWjSSNg&s"
        }
    ],
    "weatherInformation": {
                    "maxtemp_c": 11.6,
                    "maxtemp_f": 52.9,
                    "mintemp_c": 7.8,
                    "mintemp_f": 46.0,
                    "avgtemp_c": 9.6,
                    "avgtemp_f": 49.2,
                    "maxwind_mph": 17.9,
                    "maxwind_kph": 28.8,
                    "totalprecip_mm": 4.0,
                    "totalprecip_in": 0.16,
                    "avgvis_km": 9.6,
                    "avgvis_miles": 5.0,
                    "avghumidity": 77.0,
                    "daily_will_it_rain": 1,
                    "daily_chance_of_rain": 84,
                    "daily_will_it_snow": 0,
                    "daily_chance_of_snow": 0,
                    "condition": {
                        "text": "Patchy rain possible",
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/176.png",
                        "code": 1063
                    },
                    "uv": 2.0
                }
}