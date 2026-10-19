# EMA Hourly Continuation — ZK/USDT P8_12

**Symbol:** ZK/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1706 |
| net_profit_factor | 0.2942 |
| net_win_rate | 0.3804 |
| gross_profit_factor | 0.7589 |
| gross_win_rate | 0.4244 |
| sharpe_ratio | -15.8868 |
| sortino_ratio | -9.6997 |
| max_drawdown | 1.0000 |
| cagr | -0.9932 |
| net_avg_win | 6.4220 |
| net_avg_loss | -13.4038 |
| avg_hold_time_bars | 2.0592 |
| exposure | 0.1713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
