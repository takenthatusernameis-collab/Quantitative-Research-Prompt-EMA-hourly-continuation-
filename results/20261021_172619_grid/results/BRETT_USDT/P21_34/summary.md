# EMA Hourly Continuation — BRETT/USDT P21_34

**Symbol:** BRETT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.8465 |
| net_win_rate | 0.5216 |
| gross_profit_factor | 1.0784 |
| gross_win_rate | 0.5216 |
| sharpe_ratio | -0.8458 |
| sortino_ratio | -0.2091 |
| max_drawdown | 0.2744 |
| cagr | -0.0931 |
| net_avg_win | 78.7077 |
| net_avg_loss | -101.3636 |
| avg_hold_time_bars | 5.3094 |
| exposure | 0.0710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
