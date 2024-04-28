from flet import *
from custom_checkbox import CustomCheckBox

def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'
    
    #criação de um cículo personalizado com uma imagem no centro
    circle = Stack(
        controls=[
            #elemento ciruclar com gradiente
            Container(
                width = 100, 
                height = 100, 
                border_radius = 50, 
                bgcolor = 'white12' #cor de funto transparente
            ),
            Container(
                gradient = SweepGradient(
                    center = alignment.center, #centro do gradiente
                    start_angle = 0.0, #angulo inicial
                    end_angle = 3,
                    stops = [0.5, 0.5],
                    colors = ['#00000000', PINK],
                ),
                width = 100, 
                height = 100, 
                border_radius = 50,
                content = Row(alignment = 'center',
                              controls = [
                                  Container(padding = padding.all(5),
                                            bgcolor = BG,
                                            width = 90, height = 90,
                                            border_radius = 50, 
                                            content = Container(bgcolor = FG,
                                                                height = 80, width = 80,
                                                                border_radius = 40,
                                                                content = CircleAvatar(opacity = 0.8,
                                                                                       foreground_image_src = "https://images.unsplash.com/photo-1545912452-8aea7e25a3d3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
                                                                                       )
                                                                )
                                  )
                              ],
                              ),
            ),
        ]
    )
        
    #função para diminiur o tamanho do circulo
    def shrink(e):
        page_2.controls[0].width = 120 #largura do circulo
        page_2.controls[0].scale = transform.Scale(
            0.8, alignment = alignment.center_right)
        page_2.controls[0].border_radius = border_radius.only(
            topLeft = 35,
            topRight = 0,
            bottomLeft = 35,
            bottomRight = 0
        )
        page_2.update() #atualiza a pagina
    
    #função para restaurar o tamanho do circulo
    def restore(e):
        page_2.controls[0].width = 400
        page_2.controls[0].border_radius = 35
        page_2.controls[0].scale = transform.Scale(
            1, aligment = alignment.center_right)
        page_2.update()
        
    create_task_view = Container(
        content = Container(on_click = lambda _: page.go('/'),
          height = 40, width = 40,
          content = Text('x')
          )
    )
    
    tasks = Column(
        height = 400,
        scroll = 'auto',
    )
    
    #Adiciona 10 tarefas a lista
    for i in range (10):
        tasks.controls.append(
        Container(
            height = 70, #altura do container da tarefa
            width = 400, # largura
            bgcolor = BG,
            border_radius = 25,
            padding = padding.only(
                left = 20, top = 25, 
            ),
            content = CustomCheckBox( #checkbox personalizado
                color = PINK,
                label = 'Create interesting content'
            )),
        )
    
    #criação do card de categorias de tarefas
    categories_card = Row(
        scroll = 'auto' #rolamento automatico
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
    
    #conteudo da primeira pagina 
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
                        FloatingActionButton(bottom = 2, right = 20,
                            icon = icons.ADD, on_click = lambda _: page.go('/create_task')
                        )
                    ]
                )
            ],
        ),
    )
    page_1 = Container(
        width = 400,
        height = 850,
        bgcolor = BG,
        border_radius = 35,
        padding = padding.only(left = 50, top = 60, right = 200),
        
        content = Column(
            controls=[
                Row(alignment = 'end',
                    controls = [
                #botão para restaurar o tamanho do circulo
                Container(border_radius=25,
                          padding = padding.only(
                              top = 13, left = 13,),
                          height = 50,
                          width = 50,
                          border = border.all(
                              color = 'white', width = 1), #ao clicar, restaura o círculo
                          on_click = lambda e: restore(e),
                          content = Text('<') #texto do botão
                          )
                    ]
        ),
                Container(height = 20),
                circle,
                Text('Yas Alves', size = 32, weight = 'bold'),
                Container(height = 25),
                Row(controls=[
                    Icon(icons.FAVORITE_BORDER_SHARP, color = 'white60'),
                    Text('Templates', size = 15, weight = FontWeight.W_300,
                         color = 'white', font_family= 'poppins')
                ]),
                Container(height = 5),
                Row(controls = [
                    Icon(icons.CARD_TRAVEL, color= 'white60'),
                    Text('templates', size = 15, weight = FontWeight.W_300,
                         color = 'white', font_family='poppins')
                ]),
                Container(height = 5),
                Row(controls = [
                    Icon(icons.CALCULATE_OUTLINED, color= 'white60'),
                    Text('templates', size = 15, weight = FontWeight.W_300,
                         color = 'white', font_family='poppins')
                ]),
                
                Image(src=f"\images/1.png",
                      width = 300,
                      height = 200,
                      ),
                Text('Good', color = FG, font_family='poppins', ),
                Text('Consistency', size=22)
            ]
    )
    )
    #pagina 2 do aplicativo
    page_2 = Row(alignment = 'end', #alinhamento
        controls=[
            Container(
                width = 400,
                height = 850,
                bgcolor= FG,
                border_radius = 35,
                animate = animation.Animation(600, AnimationCurve.DECELERATE), #animação de decelaração
                animate_scale = animation.Animation(
                    400, curve = 'decelerate'), #animação da escala
                padding = padding.only( #preenchimento da pagina
                    top = 50, left = 20,
                    right = 20, bottom = 5
                ),
                content = Column(
                    controls = [
                        first_page_contents #conteudo da primeira pagina
                            
                    ]
                )
            )
        ]
    )
    
    #container principal do aplicativo
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
    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )
    
    #configura o manipulador de evento para a mudanção de rota
    page.on_route_change = route_change
    page.go(page.route) #navega para a rota atual
#inicializa o app
app(target = main, assets_dir = 'assets')