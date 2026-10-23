# EMA Hourly Continuation — BOME/USDT P21_50

**Symbol:** BOME/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 953 |
| net_profit_factor | 0.4721 |
| net_win_rate | 0.4502 |
| gross_profit_factor | 0.7735 |
| gross_win_rate | 0.4575 |
| sharpe_ratio | -6.2870 |
| sortino_ratio | -2.7304 |
| max_drawdown | 0.9682 |
| cagr | -0.7335 |
| net_avg_win | 20.0918 |
| net_avg_loss | -34.8440 |
| avg_hold_time_bars | 4.6506 |
| exposure | 0.2015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
