# EMA Hourly Continuation — BTT/USDT P144_200

**Symbol:** BTT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.3143 |
| net_win_rate | 0.3803 |
| gross_profit_factor | 0.8760 |
| gross_win_rate | 0.4282 |
| sharpe_ratio | -7.7743 |
| sortino_ratio | -2.1937 |
| max_drawdown | 0.9491 |
| cagr | -0.6942 |
| net_avg_win | 30.4184 |
| net_avg_loss | -59.3977 |
| avg_hold_time_bars | 5.6223 |
| exposure | 0.0961 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
