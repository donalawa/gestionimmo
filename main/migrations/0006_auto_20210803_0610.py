# Generated by Django 3.2.5 on 2021-08-03 05:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_user_societe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_article', models.CharField(max_length=60)),
                ('num_type', models.IntegerField()),
                ('nom', models.CharField(max_length=60)),
                ('denomination', models.CharField(max_length=60)),
                ('num_stock', models.CharField(max_length=10)),
                ('valeur', models.FloatField()),
                ('date_achat', models.DateField()),
                ('date_dernier_paiement', models.DateField()),
                ('accompte', models.FloatField()),
                ('statut', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ClientAnnotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statut', models.CharField(max_length=60)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClientAnnotationContenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ap', models.DateTimeField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('client_annotation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.clientannotation')),
            ],
        ),
        migrations.CreateModel(
            name='Emploi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denomination', models.CharField(max_length=60)),
                ('nom_societe', models.CharField(max_length=60)),
                ('adresse', models.CharField(max_length=60)),
                ('ville', models.CharField(max_length=30)),
                ('code_postal', models.CharField(max_length=15)),
                ('pays', models.CharField(max_length=20)),
                ('salaire_m', models.FloatField()),
                ('anciennete', models.IntegerField()),
                ('poste_actu', models.TextField()),
                ('autre_revenu', models.BooleanField(default=False)),
                ('autre_rev_sum', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Endettement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_emploi', models.CharField(max_length=15)),
                ('nom_responsable', models.CharField(max_length=30)),
                ('saisi', models.BooleanField(default=False)),
                ('faillite', models.BooleanField(default=False)),
                ('charge', models.BooleanField(default=False)),
                ('charge_sum', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statut', models.CharField(max_length=60)),
                ('num_facture', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(max_length=60)),
                ('ville', models.CharField(max_length=30)),
                ('code_postal', models.CharField(max_length=15)),
                ('pays', models.CharField(max_length=20)),
                ('anciennete', models.IntegerField()),
                ('loyer', models.FloatField()),
                ('residence', models.TextField()),
                ('residence_actu', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='societe',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.societe'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, unique=True, verbose_name='Name'),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('num_client', models.CharField(max_length=10)),
                ('statut', models.CharField(max_length=20)),
                ('phone_1', models.CharField(max_length=15)),
                ('phone_2', models.CharField(max_length=15)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('date_naissance', models.DateField()),
                ('ville_naissance', models.CharField(max_length=20)),
                ('pays_naissance', models.CharField(max_length=20)),
                ('type_piece_id', models.CharField(max_length=30)),
                ('numero_piece_id', models.CharField(max_length=10)),
                ('date_delivrance_id', models.DateField()),
                ('num_client_2', models.CharField(max_length=10)),
                ('proprietaire', models.BooleanField(default=False)),
                ('how_connu', models.TextField()),
                ('nom_boutique', models.CharField(max_length=40)),
                ('num_ref', models.CharField(max_length=10)),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.place')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('emploi', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.emploi')),
                ('endettement', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.endettement')),
                ('societe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.societe')),
            ],
        ),
        migrations.CreateModel(
            name='TypeArticleMoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modele', models.CharField(max_length=60)),
                ('marque', models.CharField(max_length=60)),
                ('code', models.CharField(max_length=60)),
                ('couleur', models.CharField(max_length=60)),
                ('societe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.societe')),
            ],
        ),
        migrations.CreateModel(
            name='TypeArticleImmobilier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=60)),
                ('dimension', models.IntegerField()),
                ('situation', models.TextField()),
                ('doc_1', models.ImageField(upload_to='static/menu/images')),
                ('doc_2', models.ImageField(upload_to='static/menu/images')),
                ('doc_3', models.ImageField(upload_to='static/menu/images')),
                ('nom_cite', models.CharField(max_length=60)),
                ('batiment', models.CharField(max_length=60)),
                ('inexistant', models.BooleanField(default=False)),
                ('etage', models.IntegerField()),
                ('porte', models.CharField(max_length=5)),
                ('plan_masse_local', models.ImageField(upload_to='static/menu/images')),
                ('societe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.societe')),
            ],
        ),
        migrations.CreateModel(
            name='Recouvrement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.article')),
            ],
        ),
        migrations.CreateModel(
            name='ProcedureContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=60)),
                ('annotation', models.TextField()),
                ('message', models.TextField()),
                ('date_emission', models.DateField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('emetteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('recouvrement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.recouvrement')),
            ],
        ),
        migrations.CreateModel(
            name='PretEndettement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_banque', models.CharField(max_length=60)),
                ('type_pret', models.CharField(max_length=60)),
                ('reste', models.FloatField()),
                ('mensualite', models.FloatField()),
                ('date', models.DateField()),
                ('endettement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.endettement')),
            ],
        ),
        migrations.CreateModel(
            name='Penalite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('somme_attendue', models.FloatField()),
                ('num_penal', models.IntegerField()),
                ('User_encaisseur', models.CharField(max_length=10)),
                ('statut', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('emetteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('facture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.facture')),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('somme', models.FloatField()),
                ('num_transaction', models.CharField(max_length=10)),
                ('date_paiement', models.DateField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('User_encaisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('facture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.facture')),
            ],
        ),
        migrations.AddField(
            model_name='facture',
            name='User_editeur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='facture',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.article'),
        ),
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statut', models.CharField(max_length=20)),
                ('article_interet', models.CharField(max_length=40)),
                ('frais_dossier', models.FloatField()),
                ('frais_montage', models.FloatField()),
                ('frais_immat', models.FloatField()),
                ('autres_tax', models.FloatField()),
                ('frais_livraison', models.FloatField()),
                ('frais_desendet', models.FloatField()),
                ('frais_autres', models.FloatField()),
                ('coeff_recouv', models.FloatField()),
                ('appele_recouvre', models.BooleanField(default=False)),
                ('pin', models.IntegerField()),
                ('dernier_appel', models.DateTimeField()),
                ('verifie', models.BooleanField(default=False)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('societe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.societe')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client')),
            ],
        ),
        migrations.CreateModel(
            name='Dadsr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField()),
                ('statut_1', models.BooleanField(default=False)),
                ('num_courrier', models.CharField(max_length=10)),
                ('date_courrier', models.DateField()),
                ('contenu', models.TextField()),
                ('statut_trait_cour', models.CharField(max_length=60)),
                ('statut_2', models.CharField(max_length=60)),
                ('statut_3', models.CharField(max_length=60)),
                ('date_enr', models.DateTimeField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.article')),
                ('facture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.facture')),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.FloatField()),
                ('taux', models.FloatField()),
                ('apport', models.FloatField()),
                ('date_emission', models.DateField()),
                ('date_fin', models.DateField()),
                ('frais_dossier', models.FloatField()),
                ('autre_frais', models.FloatField()),
                ('subvention', models.FloatField()),
                ('accompte', models.FloatField()),
                ('date_signature', models.DateField()),
                ('somme_payee', models.FloatField()),
                ('pre_qual', models.BooleanField(default=False)),
                ('struct_pret', models.BooleanField(default=False)),
                ('application_credit', models.BooleanField(default=False)),
                ('autorisation_etude', models.BooleanField(default=False)),
                ('notification_cosign', models.BooleanField(default=False)),
                ('ref_acheteur', models.BooleanField(default=False)),
                ('verif_pro', models.BooleanField(default=False)),
                ('aut_paiement_source', models.BooleanField(default=False)),
                ('aut_prel_bk', models.BooleanField(default=False)),
                ('aut_prel_cb', models.BooleanField(default=False)),
                ('lettre_eng', models.BooleanField(default=False)),
                ('plan_dom', models.BooleanField(default=False)),
                ('certif_res', models.BooleanField(default=False)),
                ('phot_fact', models.BooleanField(default=False)),
                ('att_heberg', models.BooleanField(default=False)),
                ('photo_id', models.BooleanField(default=False)),
                ('photoc_piece_id', models.BooleanField(default=False)),
                ('fdp', models.BooleanField(default=False)),
                ('photoc_crt_pro', models.BooleanField(default=False)),
                ('reg_comm', models.BooleanField(default=False)),
                ('rdb', models.BooleanField(default=False)),
                ('attest_rev', models.BooleanField(default=False)),
                ('carte_ret', models.BooleanField(default=False)),
                ('facture', models.BooleanField(default=False)),
                ('protect_vie', models.BooleanField(default=False)),
                ('protect_empl', models.BooleanField(default=False)),
                ('protoc_accord', models.BooleanField(default=False)),
                ('cond_resp_financ', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.article')),
                ('emetteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompteEndettement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_banque', models.CharField(max_length=60)),
                ('type_compte', models.CharField(max_length=30)),
                ('carte', models.BooleanField(default=False)),
                ('nom_carte', models.CharField(max_length=40)),
                ('endettement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.endettement')),
            ],
        ),
        migrations.CreateModel(
            name='ClientAnnotationContenuMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.TextField()),
                ('date_ap', models.DateTimeField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('client_annotation_contenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.clientannotationcontenu')),
            ],
        ),
        migrations.AddField(
            model_name='clientannotation',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Campagne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objet', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=60)),
                ('periodicite', models.CharField(max_length=60)),
                ('date_lancement', models.DateTimeField()),
                ('Cible', models.TextField()),
                ('Contenu', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Assurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statut', models.CharField(max_length=60)),
                ('nom', models.CharField(max_length=60)),
                ('adresse', models.CharField(max_length=60)),
                ('ville', models.CharField(max_length=60)),
                ('cp', models.CharField(max_length=60)),
                ('pays', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=60)),
                ('num_police', models.CharField(max_length=60)),
                ('somme', models.FloatField()),
                ('date_emission', models.DateField()),
                ('date_fin', models.DateField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.article')),
                ('emetteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='dossier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dossier'),
        ),
        migrations.CreateModel(
            name='ClientAppel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ap', models.DateTimeField()),
                ('obtention', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client')),
            ],
        ),
        migrations.AddField(
            model_name='clientannotation',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client'),
        ),
    ]
