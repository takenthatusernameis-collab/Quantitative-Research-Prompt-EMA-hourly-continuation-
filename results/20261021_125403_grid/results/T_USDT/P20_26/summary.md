# EMA Hourly Continuation — T/USDT P20_26

**Symbol:** T/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.6087 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 1.0653 |
| gross_win_rate | 0.5038 |
| sharpe_ratio | -3.3971 |
| sortino_ratio | -0.9768 |
| max_drawdown | 0.6990 |
| cagr | -0.3615 |
| net_avg_win | 52.9548 |
| net_avg_loss | -86.5653 |
| avg_hold_time_bars | 5.9574 |
| exposure | 0.1076 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
