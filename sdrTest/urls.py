from django.urls import path

from .import views

urlpatterns = [
    path("db/", views.SoldiersListView.as_view(), name="db"),
    path("add/",views.add,name='add'),
    path("edit/<int:id>/",views.edit,name='edit'),
    path("delete/<int:id>/",views.deleteFunc,name="delete"),
    path('details/<int:id>/',views.displayDetails,name='details'),

    # path("add_homeAddress/",views.AddAddress.as_view(),name='addHomeAddress'),

    path("add_homeAddress/<int:id>/",views.addNewAddress,name='addHomeAddress'),



    path('homeAddress/',views.displayAddress,name='homeAddress'),
    path('spouse/',views.displaySpouse,name='spouse'),
    path('pnok/',views.displaypNOK,name='pNOK'),
    path('snok/',views.displaysNOK,name='sNOK'),
    path('estateAdmin/',views.displayEstateAdmin,name='estateAdmin'),
    path('formalEduc/',views.displayFormalEduc,name='formalEduc'),
    path('militaryCrse/',views.displayMilitaryCo,name='militaryCrse'),
    path('livingChldrn/',views.displayLivingChildren,name='livingChldrn'),

]