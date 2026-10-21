# EMA Hourly Continuation — ORDI/USDT P21_55

**Symbol:** ORDI/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.6683 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.8510 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -2.9274 |
| sortino_ratio | -0.9348 |
| max_drawdown | 0.6670 |
| cagr | -0.3488 |
| net_avg_win | 57.5260 |
| net_avg_loss | -72.8301 |
| avg_hold_time_bars | 7.7520 |
| exposure | 0.1776 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
