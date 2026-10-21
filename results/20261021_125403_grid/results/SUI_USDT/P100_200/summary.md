# EMA Hourly Continuation — SUI/USDT P100_200

**Symbol:** SUI/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 237 |
| net_profit_factor | 0.6855 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.8777 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -1.6159 |
| sortino_ratio | -0.3545 |
| max_drawdown | 0.3821 |
| cagr | -0.1496 |
| net_avg_win | 63.8981 |
| net_avg_loss | -86.3977 |
| avg_hold_time_bars | 12.4684 |
| exposure | 0.1343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
