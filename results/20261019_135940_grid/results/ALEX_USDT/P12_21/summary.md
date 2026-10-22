# EMA Hourly Continuation — ALEX/USDT P12_21

**Symbol:** ALEX/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1267 |
| net_profit_factor | 0.3336 |
| net_win_rate | 0.3220 |
| gross_profit_factor | 0.8319 |
| gross_win_rate | 0.3623 |
| sharpe_ratio | -14.7094 |
| sortino_ratio | -7.4489 |
| max_drawdown | 1.0000 |
| cagr | -0.9820 |
| net_avg_win | 12.2712 |
| net_avg_loss | -17.4694 |
| avg_hold_time_bars | 3.2786 |
| exposure | 0.1888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
