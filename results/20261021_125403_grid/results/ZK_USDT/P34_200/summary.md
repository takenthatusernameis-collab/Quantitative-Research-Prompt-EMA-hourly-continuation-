# EMA Hourly Continuation — ZK/USDT P34_200

**Symbol:** ZK/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.8659 |
| net_win_rate | 0.5049 |
| gross_profit_factor | 1.0156 |
| gross_win_rate | 0.5049 |
| sharpe_ratio | -0.7697 |
| sortino_ratio | -0.1995 |
| max_drawdown | 0.2217 |
| cagr | -0.0901 |
| net_avg_win | 83.1393 |
| net_avg_loss | -97.9257 |
| avg_hold_time_bars | 33.7443 |
| exposure | 0.5018 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
