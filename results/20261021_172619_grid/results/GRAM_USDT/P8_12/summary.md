# EMA Hourly Continuation — GRAM/USDT P8_12

**Symbol:** GRAM/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 155 |
| net_profit_factor | 0.8784 |
| net_win_rate | 0.5677 |
| gross_profit_factor | 1.3076 |
| gross_win_rate | 0.5677 |
| sharpe_ratio | -0.4786 |
| sortino_ratio | -0.0868 |
| max_drawdown | 0.1574 |
| cagr | -0.0400 |
| net_avg_win | 79.9233 |
| net_avg_loss | -119.5089 |
| avg_hold_time_bars | 4.7097 |
| exposure | 0.0332 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
