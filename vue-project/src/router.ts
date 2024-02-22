import { createRouter, createWebHistory } from "vue-router";
import { defineAsyncComponent } from "vue";

const ResultChart = defineAsyncComponent(() => import("./components/pages/ResultChart.vue"));
const PatientInfo = defineAsyncComponent(() => import("./components/pages/PatientInfo.vue"));

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
    ],
});

export default router;