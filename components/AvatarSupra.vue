<template>
<div class="flex items-center gap-4">
        <div class="relative group cursor-pointer">
          <UAvatar
              src="headsupra.png"
              :chip="{
                inset: true,
                color: 'success'
              }"
              class="border-2 border-white shadow-lg transition-transform duration-300 group-hover:scale-105"
          />
        </div>
        
        <div>
          <h1 class="text-xl font-bold leading-tight tracking-wide drop-shadow-sm">Supra IA</h1>
          <div class="flex items-center gap-1">
            <span class="text-[10px] bg-white/20 px-2 py-0.5 rounded-full text-white font-medium backdrop-blur-sm">
              Online
            </span>
          </div>
        </div>
      </div>
</template>