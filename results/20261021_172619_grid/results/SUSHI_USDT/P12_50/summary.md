# EMA Hourly Continuation — SUSHI/USDT P12_50

**Symbol:** SUSHI/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.7617 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 0.9838 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -2.6624 |
| sortino_ratio | -0.9390 |
| max_drawdown | 0.6845 |
| cagr | -0.3507 |
| net_avg_win | 71.9110 |
| net_avg_loss | -87.5772 |
| avg_hold_time_bars | 12.3931 |
| exposure | 0.3438 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
