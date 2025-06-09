import glob

#lora = sorted(glob.glob('./experiment/gpt*-lora_lr1e-3*.txt'))
#slora = sorted(glob.glob('./experiment/gpt*-slora_lr1e-3*.txt'))

#lora = sorted(glob.glob('./experiment/gptj-6b-lora-math-all-r32_*.txt'))
#slora = sorted(glob.glob('./experiment/gptj-6b-slora-math-all-r32_*.txt'))

#model = 'gpt'
model = 'llama'

#dataset = 'math_10k'
dataset = 'commonsense_170k'

rank = 4

lr= 0.0002

if dataset == 'commonsense_170k':
    lora = sorted(glob.glob(f'./experiment/{model}_{dataset}_lora_r{rank}_lr{lr}_*result.txt'))
    slora = sorted(glob.glob(f'./experiment/{model}_{dataset}_slora_r{rank}_lr{lr}_*result.txt'))
else:
    lora = sorted(glob.glob(f'./experiment/{model}_{dataset}_lora_r{rank}_lr{lr}_*.txt'))
    slora = sorted(glob.glob(f'./experiment/{model}_{dataset}_slora_r{rank}_lr{lr}_*.txt'))

print(f'\n{model}_{dataset}_r{rank}_lr{lr}')

print("\n###########LoRA##########\n")

lora_results = []
slora_results = []
for i in range(len(lora)):
    l = open(lora[i], 'r')
    
    print(lora[i].split('_')[-2])

    lora_result = round(float(l.readlines()[-1].split(' ')[-1]),3)
    
    lora_results.append(lora_result)

    print(f'LoRA: {lora_result}')

print(f'AVG LoRA: {sum(lora_results)/ len(lora_results)}')

print("\n##########SLoRA##########\n")

for i in range(len(slora)):
    sl = open(slora[i], 'r')
    
    print(slora[i].split('_')[-2])

    slora_result = round(float(sl.readlines()[-1].split(' ')[-1]),3)
    
    slora_results.append(slora_result)

    print(f'SLoRA: {slora_result}')

print(f'AVG SLoRA: {sum(slora_results)/ len(slora_results)}')