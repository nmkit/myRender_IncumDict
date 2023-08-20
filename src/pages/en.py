import dash
from dash import dcc, html
import dash_bootstrap_components as dbc


eng_incum_list=['AGREEMENT FOR SALE AND PURCHASE',
 'AGREEMENT FOR SALE AND PURCHASE WITH PLAN',
 'AGREEMENT FOR SUBSALE AND PURCHASE',
 'AGREEMENT FOR SUBSALE AND SUBPURCHASE',
 'APPROVAL LETTER',
 'ASSENT',
 'ASSIGNMENT',
 'ASSIGNMENT OF RENTAL',
 'ASSIGNMENT WITH PLAN',
 'CANCELLATION AGREEMENT',
 'CARBON COPY OF PRELIMINARY SALE AND PURCHASE AGREEMENT',
 'CARBON COPY OF PROVISIONAL AGREEMENT FOR SALE AND PURCHASE',
 'CERTIFICATE OF COMPLIANCE',
 'CERTIFICATE OF EXEMPTION FROM ESTATE DUTY',
 'CERTIFICATE OF REGISTRATION OF DEATH',
 'CERTIFICATE UNDER S.33(1) OF THE BUILDINGS ORDINANCE',
 'CERTIFIED COPY OF AN ENTRY IN A REGISTER OF DEATH',
 'CERTIFIED COPY OF CERTIFICATE OF DEATH',
 'CERTIFIED COPY OF DEATH CERTIFICATE',
 'CERTIFIED COPY OF LETTER OF DETERMINATION',
 'CERTIFIED TRUE COPY OF DEATH CERTIFICATE',
 'CHINESE PROVISIONAL AGREEMENT FOR SALE AND PURCHASE',
 'CONFIRMATORY RELEASE',
 'CONSENT LETTER',
 'CONSENT TO ASSIGN',
 'DEATH CERTIFICATE',
 'DEED OF ASSENT',
 'DEED OF ASSIGNMENT',
 'DEED OF ASSIGNMENT OF RENTAL INCOME',
 'DEED OF FAMILY ARRANGEMENT',
 'DEED OF GIFT',
 'DEED OF LOAN',
 'DEED OF MUTUAL COVENANT AND MANAGEMENT AGREEMENT WITH PLAN',
 'DEED OF MUTUAL COVENANT INCORPORATING MANAGEMENT AGREEMENT WITH PLAN',
 'DEED OF RECTIFICATION',
 'DEED OF RELEASE',
 'DEED OF SEVERANCE',
 'DEED POLL',
 'DUPLICATE OF UNDERTAKING LETTER',
 'EQUITABLE MORTGAGE',
 'FINAL RELEASE',
 'FINANCE UNDERTAKING',
 'FIRE SAFETY COMPLIANCE ORDER UNDER S.6(1) OF FIRE SAFETY (BUILDINGS) ORDINANCE (CHAPTER 572)',
 'FIRST CHARGE',
 'FIRST EQUITABLE MORTGAGE',
 'FIRST LEGAL CHARGE',
 'FIRST LEGAL CHARGE/MORTGAGE',
 'FOURTH MORTGAGE',
 'FURTHER CHARGE',
 'GOVERNMENT NOTICE',
 'IRREVOCABLE POWER OF ATTORNEY',
 'LEGAL CHARGE',
 'LEGAL CHARGE/MORTGAGE',
 'LETTER FOR REMOVAL OF ALIENATION RESTRICTIONS',
 'LETTER OF COMPLIANCE',
 'LETTER OF NOMINATION',
 'LETTER OF REMOVAL OF ALIENATION RESTRICTIONS',
 'LETTER OF WITHDRAWAL',
 'LETTERS OF ADMINISTRATION',
 'LETTERS OF ADMINISTRATION DE BONIS NON',
 'LOAN AGREEMENT',
 'MEMORANDUM FOR SALE AND PURCHASE',
 'MEMORANDUM OF AGREEMENT FOR SALE AND PURCHASE',
 'MEMORANDUM OF CHARGE',
 'MEMORANDUM OF DETERMINATION',
 'MEMORANDUM OF DISCHARGE',
 'MEMORANDUM OF RELEASE',
 'MEMORANDUM OF SALE',
 'MEMORANDUM OF SALE AND PURCHASE',
 'MEMORANDUM OF SATISFACTION',
 'MEMORIAL OF SATISFACTION UNDER S.33(10) OF THE BUILDINGS ORDINANCE',
 'MORTGAGE',
 'MORTGAGE DEED',
 'MORTGAGE TO SECURE GENERAL BANKING FACILITIES',
 'MORTGAGE/LEGAL CHARGE',
 'NO OBJECTION LETTER',
 'NOMINATION',
 'NOTICE OF SEVERANCE',
 'NOTICE OF SEVERANCE OF JOINT TENANCY',
 'NOTICE UNDER S.24C(1) OF THE BUILDINGS ORDINANCE',
 'NOTICE UNDER S.30B(3) OF THE BUILDINGS ORDINANCE',
 'NOTICE UNDER S.30C(3) OF THE BUILDINGS ORDINANCE',
 'NOTIFICATION LETTER OF COMPLETION OF WORKS',
 'NOTIFICATION LETTER OF COMPLETION OF WORKS RELATING TO ORDER',
 'OCCUPATION PERMIT',
 'ORDER',
 'ORDER UNDER S.24(1) OF THE BUILDINGS ORDINANCE',
 'ORDER UNDER S.24(1) OF THE BUILDINGS ORDINANCE WITH PLAN',
 'ORDER UNDER S.26 OF THE BUILDINGS ORDINANCE',
 'ORDER UNDER S.26 OF THE BUILDINGS ORDINANCE WITH PLAN',
 'ORDER UNDER S.26A(1) OF THE BUILDINGS ORDINANCE',
 'ORDER UNDER S.26A(1) OF THE BUILDINGS ORDINANCE WITH PLAN',
 'ORDER UNDER S.27A OF THE BUILDINGS ORDINANCE WITH PLAN',
 'ORDER UNDER S.28(3) OF THE BUILDINGS ORDINANCE',
 'ORDER UNDER S.28(3) OF THE BUILDINGS ORDINANCE WITH PLAN',
 'PARTIAL RELEASE',
 'POWER OF ATTORNEY',
 'PRELIMINARY AGREEMENT FOR SALE AND PURCHASE',
 'PRELIMINARY SALE AND PURCHASE AGREEMENT',
 'PROBATE',
 'PROVISIONAL AGREEMENT FOR SALE AND PURCHASE',
 'RECEIPT ON DISCHARGE',
 'RECEIPT ON DISCHARGE OF A CHARGE',
 'RELEASE',
 'RENT ASSIGNMENT',
 'RENTAL ASSIGNMENT',
 'REREGISTRATION OF AGREEMENT FOR SALE AND PURCHASE MEMORIAL',
 'REREGISTRATION OF ASSIGNMENT MEMORIAL',
 'REVERSE MORTGAGE',
 'SALE AND PURCHASE AGREEMENT',
 'SATISFACTION LETTER',
 "SEALED COPY OF BANKRUPTCY ORDER ON DEBTOR'S PETITION",
 'SEALED COPY OF CHARGING ORDER ABSOLUTE',
 'SEALED COPY OF CHARGING ORDER: NOTICE TO SHOW CAUSE',
 'SEALED COPY OF ORDER',
 'SEALED COPY OF WRIT OF SUMMONS',
 'SECOND EQUITABLE MORTGAGE',
 'SECOND LEGAL CHARGE',
 'SECOND LEGAL CHARGE/MORTGAGE',
 'SECOND MORTGAGE',
 'SECOND SUPPLEMENTAL STATUTORY DECLARATION',
 'STATUTORY DECLARATION',
 'SUBCHARGE/SUBMORTGAGE',
 'SUBDEED OF MUTUAL COVENANT AND MANAGEMENT AGREEMENT WITH PLAN',
 'SUBDEED OF MUTUAL COVENANT WITH PLAN',
 'SUBMORTGAGE',
 'SUPERSEDING NOTICE UNDER S.30B(3) OF THE BUILDINGS ORDINANCE',
 'SUPERSEDING NOTICE UNDER S.30C(3) OF THE BUILDINGS ORDINANCE',
 'SUPERSEDING ORDER UNDER S.24(1) OF THE BUILDINGS ORDINANCE',
 'SUPERSEDING ORDER UNDER S.24(1) OF THE BUILDINGS ORDINANCE WITH PLAN',
 'SUPERSEDING ORDER UNDER S.26 OF THE BUILDINGS ORDINANCE',
 'SUPPLEMENTAL AGREEMENT',
 'SUPPLEMENTAL STATUTORY DECLARATION',
 'TENANCY AGREEMENT',
 'THIRD LEGAL CHARGE',
 'THIRD MORTGAGE',
 'THREE-PARTY MORTGAGE DEED',
 'TRANSFER OF MORTGAGE',
 'TRIPARTITE EQUITABLE MORTGAGE',
 'TRIPARTITE LEGAL CHARGE/MORTGAGE',
 'TRIPARTITE MORTGAGE/LEGAL CHARGE',
 'TRIPARTITE SECOND LEGAL CHARGE/MORTGAGE',
 'TWO-PARTY MORTGAGE DEED',
 'UNDERTAKING',
 'UNDERTAKING LETTER',
 'WAIVER LETTER']

dash.register_page(__name__, path='/', title='Incumbrance Dictionary')

layout = [dbc.Row(
        dbc.Col(html.P(
                    html.A("中文", href='/zh'
                         )
                ,className='text-end'),

        width=10)

    ),

    dbc.Row([

        dbc.Col([
            dcc.Markdown('Enter Incumbrance:'),
            dcc.Dropdown(id='my-dpdn', multi=False,placeholder='Please Enter',
                         options=[{'label': x, 'value': x}
                                  for x in eng_incum_list],
                         ),
            #dcc.Graph(id='line-fig', figure={})
            dcc.Markdown(id='simple_text', children= '{}'.format(''), style={"margin-top": "25px"} ),
            # dbc.Collapse(
            #         dbc.CardBody("Because it's a lot better than a hotdog."),
            #         id="collapse_en", is_open=True
            # ),

            html.Div(#html.H6("Product: a beautiful Pizza reheated after a day in the fridge, for $99"),
                     style={"text-align":"center"}),
                html.Hr(),
                dbc.CardHeader(
                    [
                    dbc.Button(
                        "More Details on this Incumbrance",
                        color="link",
                        id="button-question-1",
                    ),

                    ]


                ),

                dbc.Collapse(
                    dbc.CardBody(children="Please enter an Incumbrance first.",),
                    id="collapse_en", is_open=False
                ),

                html.Br(),
                html.Label(
                    ['Disclamier: This dictionary is intended for general reference purposes only and does not constitute the provision of any professional advice. Purchasing a second-hand property may involve complex legal issues, and users should carefully consider seeking advice from relevant professionals before making any decisions. The information provided in this article should not replace professional advice, and readers should assume their own risks associated with referencing this content.'
                     ],

                    ),


                html.Hr(),


                dbc.CardHeader(
                    [html.H5(
                        "Require more personalised service?",
                        #color="link",
                        id="personal_advice_header_en",
                    ),

                    html.Label(
                        ['Please ', html.A('click', href='https://www.proinfotech.net/contact/', target="_blank"), ' here.'],
                        id="advice_sent_en",
                        )
                    ]
                )




        ],  # width={'size':5, 'offset':1, 'order':1},
            xs=12, sm=12, md=12, lg=5, xl=5
        ),
    ],
justify='center')
    ]



