# EMA Hourly Continuation — PENDLE/USDT P21_55

**Symbol:** PENDLE/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.8189 |
| net_win_rate | 0.5083 |
| gross_profit_factor | 1.0331 |
| gross_win_rate | 0.5083 |
| sharpe_ratio | -1.4876 |
| sortino_ratio | -0.4968 |
| max_drawdown | 0.4712 |
| cagr | -0.2053 |
| net_avg_win | 72.0968 |
| net_avg_loss | -91.0190 |
| avg_hold_time_bars | 8.1442 |
| exposure | 0.2003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
