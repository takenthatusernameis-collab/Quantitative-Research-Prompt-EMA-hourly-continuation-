# EMA Hourly Continuation — ID/USDT P21_200

**Symbol:** ID/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.9329 |
| net_win_rate | 0.5311 |
| gross_profit_factor | 1.1200 |
| gross_win_rate | 0.5311 |
| sharpe_ratio | -0.3340 |
| sortino_ratio | -0.0839 |
| max_drawdown | 0.1634 |
| cagr | -0.0416 |
| net_avg_win | 87.3356 |
| net_avg_loss | -106.0520 |
| avg_hold_time_bars | 46.5836 |
| exposure | 0.6430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
