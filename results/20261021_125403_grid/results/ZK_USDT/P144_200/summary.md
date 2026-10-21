# EMA Hourly Continuation — ZK/USDT P144_200

**Symbol:** ZK/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 223 |
| net_profit_factor | 0.7019 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.9095 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -1.5671 |
| sortino_ratio | -0.3467 |
| max_drawdown | 0.3377 |
| cagr | -0.1468 |
| net_avg_win | 67.6826 |
| net_avg_loss | -90.5634 |
| avg_hold_time_bars | 8.5740 |
| exposure | 0.0932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
