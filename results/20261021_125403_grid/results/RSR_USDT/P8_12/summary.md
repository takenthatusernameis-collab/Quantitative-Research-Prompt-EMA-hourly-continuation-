# EMA Hourly Continuation — RSR/USDT P8_12

**Symbol:** RSR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.8343 |
| net_win_rate | 0.5382 |
| gross_profit_factor | 1.1428 |
| gross_win_rate | 0.5382 |
| sharpe_ratio | -0.8399 |
| sortino_ratio | -0.2016 |
| max_drawdown | 0.2241 |
| cagr | -0.0892 |
| net_avg_win | 71.1794 |
| net_avg_loss | -99.4238 |
| avg_hold_time_bars | 4.9964 |
| exposure | 0.0625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
