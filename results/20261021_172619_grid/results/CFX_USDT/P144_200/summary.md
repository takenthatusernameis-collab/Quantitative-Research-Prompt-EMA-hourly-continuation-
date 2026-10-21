# EMA Hourly Continuation — CFX/USDT P144_200

**Symbol:** CFX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 177 |
| net_profit_factor | 0.6141 |
| net_win_rate | 0.4520 |
| gross_profit_factor | 0.8171 |
| gross_win_rate | 0.4520 |
| sharpe_ratio | -1.9962 |
| sortino_ratio | -0.3781 |
| max_drawdown | 0.3709 |
| cagr | -0.1598 |
| net_avg_win | 70.4416 |
| net_avg_loss | -94.6044 |
| avg_hold_time_bars | 8.6554 |
| exposure | 0.0696 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
