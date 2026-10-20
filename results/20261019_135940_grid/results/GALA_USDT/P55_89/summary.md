# EMA Hourly Continuation — GALA/USDT P55_89

**Symbol:** GALA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.4135 |
| net_win_rate | 0.4182 |
| gross_profit_factor | 0.7239 |
| gross_win_rate | 0.4239 |
| sharpe_ratio | -7.1104 |
| sortino_ratio | -2.6627 |
| max_drawdown | 0.9636 |
| cagr | -0.7305 |
| net_avg_win | 23.0904 |
| net_avg_loss | -40.1396 |
| avg_hold_time_bars | 4.1465 |
| exposure | 0.1325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
