# EMA Hourly Continuation — POLYX/USDT P20_34

**Symbol:** POLYX/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.6787 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 1.0350 |
| gross_win_rate | 0.4990 |
| sharpe_ratio | -3.0498 |
| sortino_ratio | -0.9615 |
| max_drawdown | 0.6943 |
| cagr | -0.3558 |
| net_avg_win | 59.0794 |
| net_avg_loss | -85.9714 |
| avg_hold_time_bars | 5.0520 |
| exposure | 0.1105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
