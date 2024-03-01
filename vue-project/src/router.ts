import { createRouter, createWebHistory } from "vue-router";
import { defineAsyncComponent } from "vue";

const ResultChart = defineAsyncComponent(() => import("./components/pages/ResultChart.vue"));
const PatientInfo = defineAsyncComponent(() => import("./components/pages/PatientInfo.vue"));
const VietnamInfo = defineAsyncComponent(() => import("./components/pages/VietnamInfo.vue"));

const router = createRouter({
	history: createWebHistory(),
	routes: [
        {
			path: "/result",
            name: "result",
			component: ResultChart,
		},
        {
            path: "/info",
            component: PatientInfo,
        },
        {
            path: "/vietnam",
            component: VietnamInfo,
        }
    ],
});

export default router;