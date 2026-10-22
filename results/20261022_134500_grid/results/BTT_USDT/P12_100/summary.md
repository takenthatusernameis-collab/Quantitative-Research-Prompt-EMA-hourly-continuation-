# EMA Hourly Continuation — BTT/USDT P12_100

**Symbol:** BTT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.4545 |
| net_win_rate | 0.4147 |
| gross_profit_factor | 0.8868 |
| gross_win_rate | 0.4542 |
| sharpe_ratio | -6.8840 |
| sortino_ratio | -2.2818 |
| max_drawdown | 0.9491 |
| cagr | -0.6944 |
| net_avg_win | 34.2343 |
| net_avg_loss | -53.3699 |
| avg_hold_time_bars | 25.4704 |
| exposure | 0.6449 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
