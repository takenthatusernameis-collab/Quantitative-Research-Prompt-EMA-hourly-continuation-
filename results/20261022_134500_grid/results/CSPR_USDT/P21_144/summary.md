# EMA Hourly Continuation — CSPR/USDT P21_144

**Symbol:** CSPR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 773 |
| net_profit_factor | 0.4743 |
| net_win_rate | 0.4075 |
| gross_profit_factor | 0.7147 |
| gross_win_rate | 0.4114 |
| sharpe_ratio | -6.5027 |
| sortino_ratio | -2.5291 |
| max_drawdown | 0.9552 |
| cagr | -0.7069 |
| net_avg_win | 27.3263 |
| net_avg_loss | -39.6270 |
| avg_hold_time_bars | 14.0569 |
| exposure | 0.4939 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
