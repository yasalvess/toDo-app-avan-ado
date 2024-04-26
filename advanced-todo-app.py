from flet import *

def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    container
                ],
            ),
            
        )
    create_task_view = Container()
    
    tasks = Column()
    
    categories_card = Row(
        scroll= 'auto'
    )
    
    categories = ['Study', 'Hobbies', 'Growing']
    for i, category in enumerate(categories):
        categories_card.controls.append(
            Container(
                border_radius = 20,
                bgcolor = BG,
                width = 170,
                height = 110,
                padding = 15,
                content = Column(
                    controls = [
                        Text('40 Tasks'),
                        Text(category),
                        Container(
                            width = 160, 
                            height = 5,
                            bgcolor = 'white12',
                            border_radius = 20, 
                            padding = padding.only(right = i* 2),
                            content = Container(
                                bgcolor= PINK,
                            ),
                        )

                    ]
                )
            )
        )
    
    first_page_contents = Container(
        content = Column(
            controls = [
                Row(alignment = 'spaceBetween', #define um espaçõ entre o ícones
                    controls = [
                        Container(
                        content = Icon(
                            icons.MENU)),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED)
                            ],
                        ),
                       
                    ],
                ),
                Container(height = 20),
                Text(
                    value = 'What\'s up Yas!'
                ),
                Text(
                    value = 'CATEGORIES'
                ),
                Container(
                    padding = padding.only(top = 10, bottom = 20,),
                    content = categories_card
                ),
                Text('TODAY\'S TASKS'),
                Stack(
                    controls = [
                        tasks,
                        FloatingActionButton(
                            icon = icons.ADD, on_click = lambda _: page.go('/create_task')
                        )
                    ]
                )
            ],
        ),
    )
    page_1 = Container()
    page_2 = Row(
        controls=[
            Container(
                width = 350,
                height = 650,
                bgcolor= FG,
                border_radius = 35,
                padding = padding.only(
                    top = 50, left = 20,
                    right = 20, bottom = 5
                ), 
                content = Column(
                    controls = [
                        first_page_contents
                            
                    ]
                )
            )
        ]
    )
    
    container = Container(
        width = 350,
        height = 650,
        bgcolor = BG,
        border_radius = 35,
        content = Stack(
            controls = [
                page_1,
                page_2,
            ]
        )
    )
    
    pages = {
        '/':View(
            "/",
            [
                container
            ],
        ),
        '/create_task': View(
            "/create_task",
            [
                create_task_view
            ],
        )
    }
    
    page.add(container)
    
    page.on_route_change = route_change
    page.go(page.route)

app(target = main)