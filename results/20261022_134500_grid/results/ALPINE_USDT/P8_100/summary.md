# EMA Hourly Continuation — ALPINE/USDT P8_100

**Symbol:** ALPINE/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.6621 |
| net_win_rate | 0.4780 |
| gross_profit_factor | 0.9359 |
| gross_win_rate | 0.4808 |
| sharpe_ratio | -2.4962 |
| sortino_ratio | -0.6731 |
| max_drawdown | 0.5686 |
| cagr | -0.2700 |
| net_avg_win | 61.5265 |
| net_avg_loss | -85.0972 |
| avg_hold_time_bars | 46.9121 |
| exposure | 0.7762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
