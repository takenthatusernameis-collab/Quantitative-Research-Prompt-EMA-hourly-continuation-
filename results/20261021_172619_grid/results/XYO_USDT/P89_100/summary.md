# EMA Hourly Continuation — XYO/USDT P89_100

**Symbol:** XYO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 138 |
| net_profit_factor | 0.5061 |
| net_win_rate | 0.4275 |
| gross_profit_factor | 0.7933 |
| gross_win_rate | 0.4275 |
| sharpe_ratio | -2.6608 |
| sortino_ratio | -0.4473 |
| max_drawdown | 0.4433 |
| cagr | -0.1871 |
| net_avg_win | 70.6789 |
| net_avg_loss | -104.3009 |
| avg_hold_time_bars | 7.1377 |
| exposure | 0.0446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
