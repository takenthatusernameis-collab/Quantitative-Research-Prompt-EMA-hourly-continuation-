# EMA Hourly Continuation — JTO/USDT P26_55

**Symbol:** JTO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 879 |
| net_profit_factor | 0.5574 |
| net_win_rate | 0.4551 |
| gross_profit_factor | 0.9025 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -5.7301 |
| sortino_ratio | -2.4008 |
| max_drawdown | 0.9441 |
| cagr | -0.6816 |
| net_avg_win | 29.7033 |
| net_avg_loss | -44.5020 |
| avg_hold_time_bars | 4.8544 |
| exposure | 0.1940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
