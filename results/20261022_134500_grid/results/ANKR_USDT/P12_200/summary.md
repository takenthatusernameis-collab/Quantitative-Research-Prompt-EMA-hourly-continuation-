# EMA Hourly Continuation — ANKR/USDT P12_200

**Symbol:** ANKR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.6737 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 0.9599 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -2.4706 |
| sortino_ratio | -0.6171 |
| max_drawdown | 0.5364 |
| cagr | -0.2553 |
| net_avg_win | 73.9750 |
| net_avg_loss | -95.9906 |
| avg_hold_time_bars | 55.9073 |
| exposure | 0.7954 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
