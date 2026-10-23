# EMA Hourly Continuation — SLP/USDT P34_200

**Symbol:** SLP/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.5786 |
| net_win_rate | 0.4569 |
| gross_profit_factor | 0.8548 |
| gross_win_rate | 0.4634 |
| sharpe_ratio | -3.6576 |
| sortino_ratio | -1.1089 |
| max_drawdown | 0.7417 |
| cagr | -0.4131 |
| net_avg_win | 47.7805 |
| net_avg_loss | -69.4702 |
| avg_hold_time_bars | 24.0603 |
| exposure | 0.5075 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
