# EMA Hourly Continuation — KAVA/USDT P8_12

**Symbol:** KAVA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.4692 |
| net_win_rate | 0.4297 |
| gross_profit_factor | 0.8037 |
| gross_win_rate | 0.4405 |
| sharpe_ratio | -4.8663 |
| sortino_ratio | -1.3437 |
| max_drawdown | 0.7985 |
| cagr | -0.4698 |
| net_avg_win | 44.2893 |
| net_avg_loss | -71.1365 |
| avg_hold_time_bars | 6.0324 |
| exposure | 0.1015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
