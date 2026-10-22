# EMA Hourly Continuation — LISTA/USDT P8_21

**Symbol:** LISTA/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 671 |
| net_profit_factor | 0.7505 |
| net_win_rate | 0.4933 |
| gross_profit_factor | 1.0099 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -2.8390 |
| sortino_ratio | -1.0928 |
| max_drawdown | 0.7334 |
| cagr | -0.3934 |
| net_avg_win | 62.5917 |
| net_avg_loss | -81.1918 |
| avg_hold_time_bars | 6.1386 |
| exposure | 0.2014 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
