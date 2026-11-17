# EMA Hourly Continuation — NUM/USDT P21_34

**Symbol:** NUM/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1056 |
| net_profit_factor | 0.2771 |
| net_win_rate | 0.3220 |
| gross_profit_factor | 0.7124 |
| gross_win_rate | 0.3532 |
| sharpe_ratio | -13.3521 |
| sortino_ratio | -6.2268 |
| max_drawdown | 0.9997 |
| cagr | -0.9599 |
| net_avg_win | 11.2685 |
| net_avg_loss | -19.3131 |
| avg_hold_time_bars | 3.6013 |
| exposure | 0.1729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
