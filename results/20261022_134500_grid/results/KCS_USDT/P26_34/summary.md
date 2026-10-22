# EMA Hourly Continuation — KCS/USDT P26_34

**Symbol:** KCS/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1077 |
| net_profit_factor | 0.0705 |
| net_win_rate | 0.1903 |
| gross_profit_factor | 0.5312 |
| gross_win_rate | 0.3380 |
| sharpe_ratio | -20.2037 |
| sortino_ratio | -10.9642 |
| max_drawdown | 1.0000 |
| cagr | -0.9975 |
| net_avg_win | 3.6994 |
| net_avg_loss | -12.3376 |
| avg_hold_time_bars | 2.2544 |
| exposure | 0.1104 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
