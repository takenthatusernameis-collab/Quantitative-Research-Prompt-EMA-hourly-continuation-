# EMA Hourly Continuation — SUI/USDT P12_100

**Symbol:** SUI/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.6646 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9911 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -3.5950 |
| sortino_ratio | -1.2448 |
| max_drawdown | 0.7946 |
| cagr | -0.4548 |
| net_avg_win | 52.6976 |
| net_avg_loss | -73.0815 |
| avg_hold_time_bars | 21.1256 |
| exposure | 0.5886 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
