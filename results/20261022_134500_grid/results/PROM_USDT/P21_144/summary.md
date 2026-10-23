# EMA Hourly Continuation — PROM/USDT P21_144

**Symbol:** PROM/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.4163 |
| net_win_rate | 0.3846 |
| gross_profit_factor | 0.6914 |
| gross_win_rate | 0.4137 |
| sharpe_ratio | -6.5186 |
| sortino_ratio | -2.2118 |
| max_drawdown | 0.9352 |
| cagr | -0.6588 |
| net_avg_win | 29.5745 |
| net_avg_loss | -44.3963 |
| avg_hold_time_bars | 18.6034 |
| exposure | 0.4947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
