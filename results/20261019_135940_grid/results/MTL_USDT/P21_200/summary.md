# EMA Hourly Continuation — MTL/USDT P21_200

**Symbol:** MTL/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.6258 |
| net_win_rate | 0.4599 |
| gross_profit_factor | 0.9132 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -2.7847 |
| sortino_ratio | -0.7166 |
| max_drawdown | 0.5895 |
| cagr | -0.2910 |
| net_avg_win | 62.5659 |
| net_avg_loss | -85.1493 |
| avg_hold_time_bars | 43.5935 |
| exposure | 0.6648 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
