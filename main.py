# Point d'entrée pour lancer le logiciel
from gui import launch_gui

data = launch_gui()

if not data:
    print("Aucune donnée saisie ou sélection annulée.")
    exit()
    
# Lancement de Import_files avec les données récupérées
import Import_files
SettingData, PerformanceData, filtered_data = Import_files.run_import_process(data)

# Lancement de l'analyse cinématique avec les données récupérées
import Analysis
summary_results, detailled_results, movements_df = Analysis.run_kinematic_analysis(SettingData, PerformanceData, filtered_data)

# Génération d'un rapport PDF
import Report
Report.generate_report(data, SettingData, PerformanceData, filtered_data, summary_results, movements_df, detailled_results)
