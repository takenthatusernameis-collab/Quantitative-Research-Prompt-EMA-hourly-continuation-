# EMA Hourly Continuation — ZIL/USDT P8_26

**Symbol:** ZIL/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1566 |
| net_profit_factor | 0.3577 |
| net_win_rate | 0.4298 |
| gross_profit_factor | 0.8729 |
| gross_win_rate | 0.4579 |
| sharpe_ratio | -11.1275 |
| sortino_ratio | -6.2122 |
| max_drawdown | 0.9996 |
| cagr | -0.9554 |
| net_avg_win | 8.2730 |
| net_avg_loss | -17.4286 |
| avg_hold_time_bars | 3.8135 |
| exposure | 0.2715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
