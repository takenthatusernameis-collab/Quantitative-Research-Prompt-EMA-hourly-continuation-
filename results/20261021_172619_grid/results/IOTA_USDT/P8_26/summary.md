# EMA Hourly Continuation — IOTA/USDT P8_26

**Symbol:** IOTA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 761 |
| net_profit_factor | 0.7720 |
| net_win_rate | 0.5151 |
| gross_profit_factor | 1.0621 |
| gross_win_rate | 0.5151 |
| sharpe_ratio | -2.3273 |
| sortino_ratio | -0.9244 |
| max_drawdown | 0.6721 |
| cagr | -0.3449 |
| net_avg_win | 56.5092 |
| net_avg_loss | -77.7617 |
| avg_hold_time_bars | 6.4139 |
| exposure | 0.2219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
