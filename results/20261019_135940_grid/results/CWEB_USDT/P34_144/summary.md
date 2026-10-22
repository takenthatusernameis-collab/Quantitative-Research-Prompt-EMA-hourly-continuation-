# EMA Hourly Continuation — CWEB/USDT P34_144

**Symbol:** CWEB/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.6765 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.9692 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -2.7046 |
| sortino_ratio | -0.7343 |
| max_drawdown | 0.6415 |
| cagr | -0.2953 |
| net_avg_win | 69.4657 |
| net_avg_loss | -93.6437 |
| avg_hold_time_bars | 27.5041 |
| exposure | 0.4613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
