from django.urls import path 
from .import views
urlpatterns = {
    path('login/', views.login),
    path('login_post/', views.login_post),
    path('adminhome/', views.adminhome),
    path('changeps/', views.changeps),
    path('changeps_post/', views.changeps_post),
    path('approvalform/<id>', views.approvalform),
    path('approvalform_post/', views.approvalform_post),
    path('approvalformviewad/<id>', views.approvalformviewad),
    path('approvalformviewad_post', views.approvalformviewad_post),
    path('complaintreply/<id>', views.complaintreply),
    path('complaintreply_post/', views.complaintreply_post),
    path('complaintview/', views.complaintview),
    path('complaint_search/', views.complaint_search),
    path('complaintview_post/', views.complaintview_post),
    path('emailsend/', views.emailsend),
    path('emailsend_post/', views.emailsend_post),
    path('managecastadd/', views.managecastadd),
    path('managecastadd_post/', views.managecastadd_post),
    path('managecastedit/<id>', views.managecastedit),
    path('managecastedit_post/', views.managecastedit_post),
    path('deletecasting/<id>',views. deletecasting),
    path('filmsearch/',views.filmsearch),
    path('managecastingview/', views.managecastingview),
    path('managecastingview_post/', views.managecastingview_post),
    path('reviewsearch/',views.reviewsearch),
    path('reviewview/', views.reviewview),
    path('reviewview_post/', views.reviewview_post),
    path('selectedcandidates/<id>', views.selectedcandidates),
    path('selectedcandidates_post/', views.selectedcandidates_post),
    path('userdetailview/<id>', views.userdetailview),
    path('userdetailview_post/', views.userdetailview_post),
    path('userssearch/',views.userssearch),
    path('userreqview/', views.userreqview),
    path('userreqview_post/', views.userreqview_post),
    path('reqaccept/<id>',views.reqaccept),
    path('rereject/<id>',views.rereject),
    path('searchuserall/',views.searchuserall),
    path('viewuser/', views.viewuser),
    path('viewuser_post/', views.viewuser_post),

    path('userhome/', views.userhome),
    path('achievementview/', views.achievementview),
    path('achievementview_post/', views.achievementview_post),
    path('achievementsadd/', views.achievementsadd),
    path('achievementsadd_post/', views.achievementsadd_post),
    path('achievementsedit/<id>', views.achievementsedit),
    path('achievementsedit_post/<id>', views.achievementsedit_post),
    path('approvalformuse/', views.approvalformuse),
    path('approvalformuse_post/', views.approvalformuse_post),
    path('apaccept/<id>',views.apaccept),
    path('apreject/<id>',views.apreject),
    path('castingsearch/',views.castingsearch),
    path('castinginfoview/', views.castinginfoview),
    path('castinginfoview_post/', views.castinginfoview_post),
    path('changepsus/', views.changepsus),
    path('changepsus_post/', views.changepsus_post),
    path('complaintsend/<id>', views.complaintsend),
    path('complaintsearch/',views.complaintsearch),
    path('complaintsend_post/', views.complaintsend_post),
    path('complaintviewreply/', views.complaintviewreply),
    path('complaintviewreply_post/', views.complaintviewreply_post),
    path('emailview/', views.emailview),
    path('emailview_post/', views.emailview_post),
    path('registrationformadd/', views.registrationformadd),
    path('registrationform_post/', views.registrationform_post),
    path('registrationformview/', views.registrationformview),
    path('registerationedit/<id>', views.registerationedit),
    path('registrationedit_post/', views.registrationedit_post),
    path('requestform/<id>', views.requestform),
    path('requestform_post/', views.requestform_post),
    path('requeststatus/', views.requeststatus),
    path('requeststatus_post/', views.requeststatus_post),
    path('reviewviewuser/', views.reviewviewuser),
    path('reviewviewuser_post/', views.reviewviewuser_post),
    path('reviewsend/', views.reviewsend),
    path('reviewsend_post/', views.reviewsend_post),
    path('respectivecastinginfoview/<id>',views.respectivecastinginfoview),
    path('respectivecastinginfoview_post/',views.respectivecastinginfoview_post)

}




