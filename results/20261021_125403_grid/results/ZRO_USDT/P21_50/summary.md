# EMA Hourly Continuation — ZRO/USDT P21_50

**Symbol:** ZRO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.8255 |
| net_win_rate | 0.5098 |
| gross_profit_factor | 1.0303 |
| gross_win_rate | 0.5098 |
| sharpe_ratio | -1.2770 |
| sortino_ratio | -0.4078 |
| max_drawdown | 0.3771 |
| cagr | -0.1726 |
| net_avg_win | 72.2229 |
| net_avg_loss | -90.9888 |
| avg_hold_time_bars | 7.3878 |
| exposure | 0.1660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
