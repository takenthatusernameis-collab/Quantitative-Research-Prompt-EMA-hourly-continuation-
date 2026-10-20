# EMA Hourly Continuation — API3/USDT P26_89

**Symbol:** API3/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 681 |
| net_profit_factor | 0.5667 |
| net_win_rate | 0.4581 |
| gross_profit_factor | 0.8500 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -4.4530 |
| sortino_ratio | -1.6364 |
| max_drawdown | 0.8650 |
| cagr | -0.5407 |
| net_avg_win | 35.9825 |
| net_avg_loss | -53.6838 |
| avg_hold_time_bars | 10.8076 |
| exposure | 0.3345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
