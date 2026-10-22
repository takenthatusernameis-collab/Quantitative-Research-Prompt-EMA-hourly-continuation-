# EMA Hourly Continuation — EWT/USDT P100_144

**Symbol:** EWT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 176 |
| net_profit_factor | 0.5998 |
| net_win_rate | 0.4375 |
| gross_profit_factor | 0.7784 |
| gross_win_rate | 0.4375 |
| sharpe_ratio | -2.1177 |
| sortino_ratio | -0.3987 |
| max_drawdown | 0.4074 |
| cagr | -0.1679 |
| net_avg_win | 71.9757 |
| net_avg_loss | -93.3337 |
| avg_hold_time_bars | 8.9091 |
| exposure | 0.0713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
