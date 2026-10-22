# EMA Hourly Continuation — ETN/USDT P50_55

**Symbol:** ETN/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 118 |
| net_profit_factor | 0.4456 |
| net_win_rate | 0.3729 |
| gross_profit_factor | 0.5893 |
| gross_win_rate | 0.3729 |
| sharpe_ratio | -2.9073 |
| sortino_ratio | -0.4881 |
| max_drawdown | 0.3796 |
| cagr | -0.2032 |
| net_avg_win | 69.3408 |
| net_avg_loss | -92.5231 |
| avg_hold_time_bars | 5.4237 |
| exposure | 0.0348 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
