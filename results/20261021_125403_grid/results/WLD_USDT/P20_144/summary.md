# EMA Hourly Continuation — WLD/USDT P20_144

**Symbol:** WLD/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 1.0851 |
| net_win_rate | 0.5546 |
| gross_profit_factor | 1.2320 |
| gross_win_rate | 0.5546 |
| sharpe_ratio | 0.5328 |
| sortino_ratio | 0.1428 |
| max_drawdown | 0.1369 |
| cagr | 0.0566 |
| net_avg_win | 100.5791 |
| net_avg_loss | -115.3987 |
| avg_hold_time_bars | 35.9617 |
| exposure | 0.5541 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
