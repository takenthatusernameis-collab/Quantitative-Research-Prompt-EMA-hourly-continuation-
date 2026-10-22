# EMA Hourly Continuation — CSPR/USDT P21_89

**Symbol:** CSPR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.7508 |
| net_win_rate | 0.4853 |
| gross_profit_factor | 0.9276 |
| gross_win_rate | 0.4853 |
| sharpe_ratio | -1.9215 |
| sortino_ratio | -0.6188 |
| max_drawdown | 0.5634 |
| cagr | -0.2486 |
| net_avg_win | 62.4715 |
| net_avg_loss | -78.4427 |
| avg_hold_time_bars | 13.2200 |
| exposure | 0.3059 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
