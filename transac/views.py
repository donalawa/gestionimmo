from django.db.models.expressions import F
from django.forms.widgets import DateInput
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users
from .forms import ClientForms,PlaceForm,EmploiForm,EndettementForm
from main.models import Client,Place,Emploi,Endettement,CompteEndettement,PretEndettement, Dossier, Cosignataire,Article
from django.core.mail import send_mail
import uuid
import random


# Declaring Global Variables.
section           = 'transac'
errors            = ''
globvar           = 0
proprietaire      = False
parents           = False
charges           = False
compte            = False
nom_banque        = None,
type_compte       = None,
article_interet   = None
clientData        = None
currentDossier    = None
clientForm        = ClientForms()
placeForm         = PlaceForm()
emploiForm        = EmploiForm()
endettementForm   = EndettementForm()



@login_required
def index(request):
      if(request.user.poste == section):  
            articles = Article.objects.all()
            return render(request, 'transac/tcompte.html', { 'title': 'Espace ouverture compte','clientForm':ClientForms,'article_interet':articles})
      else:
            return redirect(f"/login?next=/{section}/")

@login_required
def registerAccount(request,table=None,type=None):

      if(request.method == 'POST' and request.user.poste == section):
            global globvar,clientForm,emploiForm,placeForm,endettementForm,proprietaire,parents,charges,compte,nom_banque,type_compte,clientData, article_interet
            
            
            if globvar>=4:
                  globvar = 0
            data_type = request.path.split('/')[-1]          
            data_type = table          
            
            if (data_type == 'client'):                
                  globvar = globvar + 1
                  clientForm = ClientForms(request.POST)
                  if type=="True":
                        article_interet = request.POST['article_interet']
                  
            if (data_type == 'emploi'):
                  globvar = globvar + 1
                  emploiForm = EmploiForm(request.POST)

            if (data_type == 'place'):
                  globvar = globvar + 1
                  placeForm = PlaceForm(request.POST)
                  proprietaire = request.POST['proprietaire']
                  parents = request.POST['parents']
                  
            if (data_type == 'endettement'):
                  globvar = globvar + 1
                  nom_banque = request.POST['nom_banque']
                  charges = request.POST['charge']
                  compte = request.POST['compte']
                  type_compte = request.POST['type_compte']
                  endettementForm = EndettementForm(request.POST)


            print(globvar)
            if(globvar==4):
                  client_check = clientForm.is_valid()
                  emploi_check = emploiForm.is_valid()
                  place_check  = placeForm.is_valid()
                  dette_check  = endettementForm.is_valid()

  
                  if  client_check and place_check and emploi_check and dette_check :



                        new_endettement = Endettement(
                              phone_emploi            = endettementForm.cleaned_data.get('phone_emploi'),
                              nom_responsable         = endettementForm.cleaned_data.get('nom_responsable'),
                              saisi                   = endettementForm.cleaned_data.get('saisi'),
                              faillite                = endettementForm.cleaned_data.get('faillite'),
                              charge                  = charges,
                              charge_sum              = endettementForm.cleaned_data.get('phone_emploi'),
                        )

                        new_endettement.save()

                        new_emploi = Emploi(
                              denomination            = emploiForm.cleaned_data.get('denomination'),
                              nom_societe             = emploiForm.cleaned_data.get('nom_societe'),
                              adresse                 = emploiForm.cleaned_data.get('adresse'),
                              ville                   = emploiForm.cleaned_data.get('ville'),
                              pays                    = emploiForm.cleaned_data.get('pays'),
                              salaire_m               = emploiForm.cleaned_data.get('salaire_m'),
                              anciennete              = emploiForm.cleaned_data.get('anciennete'),
                              poste_actu              = emploiForm.cleaned_data.get('poste_actu'),
                              autre_revenu            = emploiForm.cleaned_data.get('autre_revenu'),
                              autre_rev_sum           = emploiForm.cleaned_data.get('autre_revenu_sum'),
                              ancien_denomination     = emploiForm.cleaned_data.get('ancien_denomination'),
                              ancien_nom_societe      = emploiForm.cleaned_data.get('ancien_nom_societe'),
                              ancien_adresse          = emploiForm.cleaned_data.get('ancien_adresse'),
                              ancien_ville            = emploiForm.cleaned_data.get('ancien_ville'),
                              ancien_code_postal      = emploiForm.cleaned_data.get('ancien_code_postal'),                          
                              ancien_pays             = emploiForm.cleaned_data.get('ancien_pays'),
                              ancien_salaire_m        = emploiForm.cleaned_data.get('ancien_salaire_m'),
                              ancien_anciennete       = emploiForm.cleaned_data.get('ancien_anciennete'),

                        )

                        new_emploi.save()


                        new_place = Place(
                              adresse                 = placeForm.cleaned_data.get('adresse'),
                              ancienne_address        = placeForm.cleaned_data.get('ancienne_address'),
                              ville                   = placeForm.cleaned_data.get('ville'),
                              ancienne_ville          = placeForm.cleaned_data.get('ancienne_ville'),
                              pays                    = placeForm.cleaned_data.get('pays'),
                              ancienne_pays           = placeForm.cleaned_data.get('ancienne_pays'),
                              loyer                   = placeForm.cleaned_data.get('loyer'),
                              ancienne_loyer          = placeForm.cleaned_data.get('ancienne_loyer'),
                              code_postal             = placeForm.cleaned_data.get('code_postal'),
                              ancienne_code_postal    = placeForm.cleaned_data.get('ancienne_code_postal'),
                              anciennete              = placeForm.cleaned_data.get('anciennete'),
                              ancienne_anciennete     = placeForm.cleaned_data.get('ancienne_anciennete'),
                        )

                        new_place.save()

                        # Register either the client or the cosigner

                        if type=="True":
                              # Storing a new Client
                              new_client = Client(
                                    societe                 = request.user.societe,
                                    User                    = request.user,
                                    nom                     = clientForm.cleaned_data.get('nom'),
                                    prenom                  = clientForm.cleaned_data.get('prenom'),
                                    email                   = clientForm.cleaned_data.get('email'),
                                    phone_1                 = clientForm.cleaned_data.get('phone_1'),
                                    phone_2                 = clientForm.cleaned_data.get('phone_2'),
                                    how_connu               = clientForm.cleaned_data.get('how_connu'),
                                    date_naissance          = clientForm.cleaned_data.get('date_naissance'),
                                    ville_naissance         = clientForm.cleaned_data.get('ville_naissance'),
                                    type_piece_id           = clientForm.cleaned_data.get('type_piece_id'),
                                    numero_piece_id         = clientForm.cleaned_data.get('numero_piece_id'),
                                    pays_naissance          = placeForm.cleaned_data.get('pays'),
                                    parents                 = bool(parents),
                                    proprietaire            = bool(proprietaire),
                                    place                   = new_place,
                                    emploi                  = new_emploi,
                                    endettement             = new_endettement, 
                                    uid                     = int(random.random()*1000000000)                       
                              )

                              new_client.save()
                              
                              clientData = new_client

                        else:
                              # Saving and assigning a clients Cosigner
                              new_cosigner = Cosignataire(
                                    societe                 = request.user.societe,
                                    User                    = request.user,
                                    nom                     = clientForm.cleaned_data.get('nom'),
                                    prenom                  = clientForm.cleaned_data.get('prenom'),
                                    email                   = clientForm.cleaned_data.get('email'),
                                    phone_1                 = clientForm.cleaned_data.get('phone_1'),
                                    phone_2                 = clientForm.cleaned_data.get('phone_2'),
                                    how_connu               = clientForm.cleaned_data.get('how_connu'),
                                    date_naissance          = clientForm.cleaned_data.get('date_naissance'),
                                    ville_naissance         = clientForm.cleaned_data.get('ville_naissance'),
                                    type_piece_id           = clientForm.cleaned_data.get('type_piece_id'),
                                    numero_piece_id         = clientForm.cleaned_data.get('numero_piece_id'),
                                    pays_naissance          = placeForm.cleaned_data.get('pays'),
                                    parents                 = bool(parents),
                                    proprietaire            = bool(proprietaire),
                                    place                   = new_place,
                                    emploi                  = new_emploi,
                                    endettement             = new_endettement,                        
                              )
                              new_cosigner.save() 
                              clientData.cosigner = new_cosigner
                              clientData.save()    

                              # Creating the Clients Dossier
                              article_interet = article_interet.split('-')[-1]
                              for article in Article.objects.all():
                                    if article.nom == article_interet:

                                          new_dossier = Dossier(
                                                societe                 = request.user.societe,             
                                                User                    = request.user,             
                                                client                  = clientData,
                                                article_interet         = article,
                                                statut                  = 'A',          
                                                coeff_recouv            = 0,   
                                                # appele_recouvre         = '',  
                                                pin                     = 0,    
                                                # dernier_appel           = '',  
                                                verifie                 = False, 
                                                uid                     = int(random.random()*1000000000)
                                                )

                                          new_dossier.save()
                                          currentDossier = new_dossier

                        new_compte_endettement = CompteEndettement(
                              endettement             = new_endettement,
                              nom_banque              = nom_banque,
                              type_compte             = type_compte,
                              compte                  = compte,
                              nom_compte              = endettementForm.cleaned_data.get('nom_compte'),
                        )

                        # new_compte_endettement.save()

                        PretEndettement(
                              endettement             = new_endettement,
                              nom_banque              = nom_banque,
                              type_pret               = endettementForm.cleaned_data.get('type_pret'),
                              reste                   = endettementForm.cleaned_data.get('reste'),
                              mensualite              = endettementForm.cleaned_data.get('mensualite'),
                              nom_banque_1            = endettementForm.cleaned_data.get('nom_banque_1'),
                              type_pret_1             = endettementForm.cleaned_data.get('type_pret_1'),
                              reste_1                 = endettementForm.cleaned_data.get('reste_1'),
                              mensualite_1            = endettementForm.cleaned_data.get('mensualite_1'),
                              nom_banque_2            = endettementForm.cleaned_data.get('nom_banque_2'),
                              type_pret_2             = endettementForm.cleaned_data.get('type_pret_2'),
                              reste_2                 = endettementForm.cleaned_data.get('reste_2'),
                              mensualite_2            = endettementForm.cleaned_data.get('mensualite_2'),
                              date                    = endettementForm.cleaned_data.get('date'),

                        )
                  else:
                        errors = f'Info Perso Client <br />{clientForm.errors}<br />Info Address Client <br />{placeForm.errors}<br />Info Emploi <br /> {emploiForm.errors} <br /> Info Endettement <br /> {endettementForm.errors} <br /> '                   
                       
                        return HttpResponse(errors)

            return HttpResponse('')


@login_required
def sendMail(request):
      if(request.method == 'POST' and request.user.poste == section):
            print(request.POST)
             
            send_mail(
                  subject="Django Email Test",# subject
                  message="Yo, hello from the real world, it just so happens that i am testing out django right now", # message
                  from_email="karlsedoide@gmail.com",# from email
                  recipient_list=['dzekarlson@gmail.com']# To mail
            )
      else:
            pass




@login_required
def vente(request):
      if(request.user.poste == section):
            print('---------------------------------')
            print(clientData)
            print('---------------------------------')

            if request.method == 'POST':
                  print('-------------Post ----------------')
                  print(clientData)
                  print(request.POST)
                  print('---------------------------------')
            else:
                  pass

            all_dossier = Dossier.objects.all()
            all_articles = Article.objects.all()

            for dossier in all_dossier:
                  print(dossier)



            return render(request, 'transac/tvente.html', { 'title': 'Espace vente','clientData':clientData,'article':all_articles,'dossier':currentDossier})
      else:
            return redirect(f"/login?next=/{section}/")




@login_required
def penalties(request):
      if(request.user.poste == section):
            return render(request, 'transac/tpenalties.html', { 'title': 'P??nalit??s'})
      else:
            return redirect(f"/login?next=/{section}/")




@login_required
def payments(request):
      if(request.user.poste == section):
            return render(request, 'transac/tpaiement.html', { 'title': 'Paiements'})
      else:
            return redirect(f"/login?next=/{section}/")




@login_required
def mutations(request):
      if(request.user.poste == section):
            return render(request, 'transac/tmutations.html', { 'title': 'Mutations'})
      else:
            return redirect(f"/login?next=/{section}/")




@login_required
def restructure(request):
      if(request.user.poste == section):
            return render(request, 'transac/trestructurations.html', { 'title': 'Restructurations'})
      else:
            return redirect(f"/login?next=/{section}/")




@login_required
def plan(request):
      if(request.user.poste == section):
            return render(request, 'transac/tpml.html', { 'title': 'Plan de masse local'})
      else:
            return redirect(f"/login?next=/{section}/")




# @login_required 
def dossiers_credit(request):
      if(request.user.poste == section):
            return render(request, 'transac/tdc.html', { 'title': 'Dossiers cr??dits (DC)'})
      else:
            return redirect(f"/login?next=/{section}/")




@login_required
def dossiers(request):
      if(request.user.poste == section):
            return render(request, 'transac/tdcpt.html', { 'title': 'Dossiers cr??dits propri??taires terriens (DCPT)'})
      else:
            return redirect(f"/login?next=/{section}/")



