# EMA Hourly Continuation — DCR/USDT P26_34

**Symbol:** DCR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.6070 |
| net_win_rate | 0.4830 |
| gross_profit_factor | 0.9846 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -3.0103 |
| sortino_ratio | -0.7769 |
| max_drawdown | 0.6113 |
| cagr | -0.2990 |
| net_avg_win | 58.6075 |
| net_avg_loss | -90.1923 |
| avg_hold_time_bars | 5.0588 |
| exposure | 0.0739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
