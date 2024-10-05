<template>
    <header class="fixed inset-x-0 top-0 z-50 ">
        <nav class="mx-auto flex max-w-7xl items-center justify-between p-6 lg:px-8" aria-label="Global">
            <div class="flex lg:flex-1">
                <a href="#" class="-m-1.5 p-1.5">
                    <span class="sr-only">Consulper Uruguay</span>
                    <img class="h-8 w-auto" src="https://tailwindui.com/plus/img/logos/mark.svg?color=indigo&shade=600"
                        alt="" />
                </a>
            </div>
            <div class="flex lg:hidden">
                <button type="button"
                    class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-50"
                    @click="mobileMenuOpen = true">
                    <span class="sr-only">Abrir el menú principal</span>
                    <Bars3Icon class="h-6 w-6" aria-hidden="true" />
                </button>
            </div>
            <PopoverGroup class="hidden lg:flex lg:gap-x-12">
                <Popover class="relative">
                    <PopoverButton class="flex items-center gap-x-1 text-sm font-semibold leading-6 text-gray-50">
                        Servicios
                        <ChevronDownIcon class="h-5 w-5 flex-none text-gray-400" aria-hidden="true" />
                    </PopoverButton>

                    <transition enter-active-class="transition ease-out duration-200"
                        enter-from-class="opacity-0 translate-y-1" enter-to-class="opacity-100 translate-y-0"
                        leave-active-class="transition ease-in duration-150"
                        leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-1">
                        <PopoverPanel
                            class="absolute -left-8 top-full z-10 mt-3 w-80 rounded-3xl bg-white bg-opacity-60 p-4 shadow-lg ring-1 ring-gray-900/5">
                            <div v-if="isLoading">Cargando servicios...</div>
                            <div v-else-if="error">Error al cargar servicios, por favor inténtelo más tarde</div>
                            <div v-for="service in data" :key="service.slug"
                                class="relative rounded-lg p-4 hover:bg-gray-50">
                                <a :href="service.get_absolute_url" class="block text-sm font-semibold leading-6 text-gray-900">
                                    {{ service.service_name }}
                                    <span class="absolute inset-0" />
                                </a>
                                <p class="mt-1 text-sm leading-6 text-gray-600">{{ service.description }}</p>
                            </div>
                        </PopoverPanel>
                    </transition>
                </Popover>
                <Popover class="relative">
                    <PopoverButton class="flex items-center gap-x-1 text-sm font-semibold leading-6 text-gray-50">
                        Sobre Nosotros
                        <ChevronDownIcon class="h-5 w-5 flex-none text-gray-400" aria-hidden="true" />
                    </PopoverButton>

                    <transition enter-active-class="transition ease-out duration-200"
                        enter-from-class="opacity-0 translate-y-1" enter-to-class="opacity-100 translate-y-0"
                        leave-active-class="transition ease-in duration-150"
                        leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-1">
                        <PopoverPanel
                            class="absolute -left-8 top-full z-10 mt-3 w-screen max-w-md overflow-hidden rounded-3xl bg-white shadow-lg ring-1 ring-gray-900/5">
                            <div class="p-4">
                                <div v-for="item in about" :key="item.name"
                                    class="group relative flex gap-x-6 rounded-lg p-4 text-sm leading-6 hover:bg-gray-50">
                                    <div
                                        class="mt-1 flex h-11 w-11 flex-none items-center justify-center rounded-lg bg-gray-50 group-hover:bg-white">
                                        <component :is="item.icon"
                                            class="h-6 w-6 text-gray-600 group-hover:text-indigo-600"
                                            aria-hidden="true" />
                                    </div>
                                    <div class="flex-auto">
                                        <a :href="item.href" class="block font-semibold text-gray-900">
                                            {{ item.name }}
                                            <span class="absolute inset-0" />
                                        </a>
                                        <p class="mt-1 text-gray-600">{{ item.description }}</p>
                                    </div>
                                </div>
                            </div>
                        </PopoverPanel>
                    </transition>
                </Popover>

                <a href="#" class="text-sm font-semibold leading-6 text-gray-50">Empleos</a>
                <a href="#" class="text-sm font-semibold leading-6 text-gray-50">Blog</a>

                
            </PopoverGroup>
            <div class="hidden lg:flex lg:flex-1 lg:justify-end">
                <a href="#" class="text-sm font-semibold leading-6 text-gray-50">Contacto<span
                        aria-hidden="true">&rarr;</span></a>
            </div>
        </nav>
        <Dialog class="lg:hidden" @close="mobileMenuOpen = false" :open="mobileMenuOpen">
            <div class="fixed inset-0 z-10" />
            <DialogPanel
                class="fixed inset-y-0 right-0 z-50 w-3/5 overflow-y-auto bg-white px-6 py-6 sm:max-w-sm sm:ring-1 sm:ring-gray-900/10">
                <div class="p-6">
                    <div class="flex items-center justify-between">
                        <a href="#" class="-m-1.5 p-1.5">
                            <span class="sr-only">Your Company</span>
                            <img class="h-8 w-auto"
                                src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="" />
                        </a>
                        <button type="button" class="-m-2.5 rounded-md p-2.5 text-gray-700"
                            @click="mobileMenuOpen = false">
                            <span class="sr-only">Cerrar meú</span>
                            <XMarkIcon class="h-6 w-6" aria-hidden="true" />
                        </button>
                    </div>
                    <div class="mt-6 flow-root">
                        <div class="-my-6 divide-y divide-gray-500/10">
                            <div class="space-y-2 py-6">
                                <a v-for="item in about" :key="about.name" :href="item.href"
                                    class="group -mx-3 flex items-center gap-x-6 rounded-lg p-3 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">
                                    <div
                                        class="flex h-11 w-11 flex-none items-center justify-center rounded-lg bg-gray-50 group-hover:bg-white">
                                        <component :is="item.icon"
                                            class="h-6 w-6 text-gray-600 group-hover:text-indigo-600"
                                            aria-hidden="true" />
                                    </div>
                                    {{ item.name }}
                                </a>
                            </div>
                            <div class="space-y-2 py-6">
                                <a href="#"
                                    class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">Empleos</a>
                                <a href="#"
                                    class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">Blog</a>

                                <a v-for="service in data" :key="service.service_name" :href="service.get_absolute_url"
                                    class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">{{
                                    service.service_name }}</a>
                            </div>
                            <div class="py-6">
                                <a href="#"
                                    class="-mx-3 block rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">Contacto</a>
                            </div>
                        </div>
                    </div>
                </div>
            </DialogPanel>
        </Dialog>
    </header>
</template>

<script setup>
import { ref } from 'vue'
import { Dialog, DialogPanel, Popover, PopoverButton, PopoverGroup, PopoverPanel } from '@headlessui/vue'
import {
    WrenchScrewdriverIcon,
    Bars3Icon,
    UserGroupIcon,
    BookOpenIcon,
    ShieldCheckIcon,
    ClipboardDocumentCheckIcon,
    XMarkIcon,
} from '@heroicons/vue/24/outline'
import { ChevronDownIcon, PhoneIcon, PlayCircleIcon } from '@heroicons/vue/20/solid'

import useFetchServices from '../services/services-api.ts';
const servicesUrl = 'http://127.0.0.1:8000/api/v1/services/'
const { isLoading, error, data } = useFetchServices(servicesUrl);

const about = [
    { name: 'Quiénes somos', description: 'Nuestro servicio, misión y código de ética', href: 'https://google.com', icon: UserGroupIcon },
    { name: 'Legal', description: 'Registro legal y cumplimiento de leyes', href: 'https://google.com', icon: BookOpenIcon },
    { name: 'Certificados', description: 'Certificados ISO y obras civíles’ data will be safe and secure', href: 'https://google.com', icon: 	ShieldCheckIcon },
    { name: 'Calidad', description: 'Trabajos hechos con los más altos estándares del mercado', href: 'https://google.com', icon: ClipboardDocumentCheckIcon },
    { name: 'Equipamento', description: 'Conoce con qué trabajamos', href: 'https://google.com', icon: WrenchScrewdriverIcon },
]
const callsToAction = [
    { name: 'Watch demo', href: '#', icon: PlayCircleIcon },
    { name: 'Contact sales', href: '#', icon: PhoneIcon },
]

const mobileMenuOpen = ref(false)
</script>