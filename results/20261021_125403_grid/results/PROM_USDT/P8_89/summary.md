# EMA Hourly Continuation — PROM/USDT P8_89

**Symbol:** PROM/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.6370 |
| net_win_rate | 0.4456 |
| gross_profit_factor | 0.8369 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -3.6838 |
| sortino_ratio | -1.2745 |
| max_drawdown | 0.7791 |
| cagr | -0.4458 |
| net_avg_win | 50.9812 |
| net_avg_loss | -64.3191 |
| avg_hold_time_bars | 21.9246 |
| exposure | 0.5950 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
