# EMA Hourly Continuation — SYN/USDT P100_144

**Symbol:** SYN/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.5306 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.8865 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -4.2828 |
| sortino_ratio | -1.3422 |
| max_drawdown | 0.8114 |
| cagr | -0.4728 |
| net_avg_win | 39.9945 |
| net_avg_loss | -65.0204 |
| avg_hold_time_bars | 4.9754 |
| exposure | 0.1104 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
