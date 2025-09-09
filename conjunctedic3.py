# Listas de tarefas das equipes
equipe_a = {"planejar reunião", "revisar documento", "testar sistema"}
equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}

# União das tarefas
tarefas_unificadas = equipe_a.union(equipe_b)

# Exibe as tarefas atuais
print("Tarefas combinadas:", tarefas_unificadas)

# Solicita a tarefa a ser removida
tarefa_remover = input("Digite a tarefa que deseja remover: ").strip().lower()

# Tenta remover a tarefa (caso exista)
tarefas_unificadas = {tarefa for tarefa in tarefas_unificadas if tarefa.lower() != tarefa_remover}

# Exibe o resultado final
print("\nTarefas finais:", tarefas_unificadas)