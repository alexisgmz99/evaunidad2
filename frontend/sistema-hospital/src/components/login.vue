<template>
<!-- https://play.tailwindcss.com/MIwj5Sp9pw -->
<div class="py-16">
    <div class="flex bg-white rounded-lg shadow-lg overflow-hidden mx-auto max-w-sm lg:max-w-4xl">
    
        <div class="hidden lg:block lg:w-1/2 bg-cover"
            style="background-image:url('https://health.gov/sites/default/files/styles/600_wide/public/2022-06/cadqt.jpg?itok=zn27s5mX.jpg')">
        </div>
        <div class="w-full p-8 lg:w-1/2">
            <h2 class="text-2xl font-semibold text-gray-700 text-center">INICIAR SESION</h2>
        
            
            <div class="mt-4">
                <label class="block text-gray-700 text-sm font-bold mb-2">Email</label>
                <input class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="email" />
            </div>
            <div class="mt-4">
                <div class="flex justify-between">
                    <label class="block text-gray-700 text-sm font-bold mb-2">Contraseña</label>
                   
                </div>
                 
                <input class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none" type="password" />
            </div>
                    <a href="#" class="text-xs text-gray-500">¿Olvidaste tu Contraseña?</a>
            <div class="mt-8">
                <button class="bg-gray-700 text-white font-bold py-2 px-4 w-full rounded hover:bg-gray-600">Iniciar Sesión</button>
            </div>
            <div class="mt-4 flex items-center justify-between">
                <span class="border-b w-1/5 md:w-1/4"></span>
                <RouterLink to="/register">                
                    <a href="" class="text-xs text-gray-500 uppercase">Aun no tienes cuenta?</a>
                </RouterLink>
                <span class="border-b w-1/5 md:w-1/4"></span>
            </div>
        </div>
    </div>
</div>
</template>