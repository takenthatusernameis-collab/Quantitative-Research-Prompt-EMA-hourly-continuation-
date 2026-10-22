# EMA Hourly Continuation — ALGO/USDT P8_21

**Symbol:** ALGO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1621 |
| net_profit_factor | 0.3414 |
| net_win_rate | 0.4454 |
| gross_profit_factor | 0.7920 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -10.9218 |
| sortino_ratio | -6.1966 |
| max_drawdown | 0.9996 |
| cagr | -0.9562 |
| net_avg_win | 7.1759 |
| net_avg_loss | -16.8822 |
| avg_hold_time_bars | 2.8519 |
| exposure | 0.2101 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
