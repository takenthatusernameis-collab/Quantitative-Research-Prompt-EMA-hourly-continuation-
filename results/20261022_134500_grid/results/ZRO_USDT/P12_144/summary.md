# EMA Hourly Continuation — ZRO/USDT P12_144

**Symbol:** ZRO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.7371 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9789 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -2.0320 |
| sortino_ratio | -0.6364 |
| max_drawdown | 0.5091 |
| cagr | -0.2614 |
| net_avg_win | 62.8740 |
| net_avg_loss | -82.7346 |
| avg_hold_time_bars | 29.3900 |
| exposure | 0.6603 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
