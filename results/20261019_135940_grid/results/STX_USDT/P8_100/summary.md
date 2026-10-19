# EMA Hourly Continuation — STX/USDT P8_100

**Symbol:** STX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.6421 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9106 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -3.3530 |
| sortino_ratio | -1.1612 |
| max_drawdown | 0.7868 |
| cagr | -0.4248 |
| net_avg_win | 46.2247 |
| net_avg_loss | -66.3085 |
| avg_hold_time_bars | 25.1232 |
| exposure | 0.6923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
