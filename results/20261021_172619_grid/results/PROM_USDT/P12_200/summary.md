# EMA Hourly Continuation — PROM/USDT P12_200

**Symbol:** PROM/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.5886 |
| net_win_rate | 0.4351 |
| gross_profit_factor | 0.7588 |
| gross_win_rate | 0.4351 |
| sharpe_ratio | -3.2959 |
| sortino_ratio | -0.9486 |
| max_drawdown | 0.6856 |
| cagr | -0.3574 |
| net_avg_win | 53.0058 |
| net_avg_loss | -69.3620 |
| avg_hold_time_bars | 34.7043 |
| exposure | 0.6562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
