# EMA Hourly Continuation — TRAC/USDT P34_50

**Symbol:** TRAC/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.6534 |
| net_win_rate | 0.4929 |
| gross_profit_factor | 0.9226 |
| gross_win_rate | 0.4929 |
| sharpe_ratio | -1.9468 |
| sortino_ratio | -0.4688 |
| max_drawdown | 0.4385 |
| cagr | -0.1919 |
| net_avg_win | 56.1893 |
| net_avg_loss | -83.5929 |
| avg_hold_time_bars | 7.7447 |
| exposure | 0.0993 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
