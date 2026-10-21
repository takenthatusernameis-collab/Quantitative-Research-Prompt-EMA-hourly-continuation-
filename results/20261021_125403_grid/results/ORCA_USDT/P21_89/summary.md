# EMA Hourly Continuation — ORCA/USDT P21_89

**Symbol:** ORCA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.7715 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 0.9928 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -1.6940 |
| sortino_ratio | -0.5383 |
| max_drawdown | 0.5091 |
| cagr | -0.2214 |
| net_avg_win | 63.0233 |
| net_avg_loss | -83.3536 |
| avg_hold_time_bars | 16.6626 |
| exposure | 0.3749 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
