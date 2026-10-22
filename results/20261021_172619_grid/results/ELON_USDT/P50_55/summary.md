# EMA Hourly Continuation — ELON/USDT P50_55

**Symbol:** ELON/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 80 |
| net_profit_factor | 0.4949 |
| net_win_rate | 0.4125 |
| gross_profit_factor | 0.6859 |
| gross_win_rate | 0.4125 |
| sharpe_ratio | -1.8750 |
| sortino_ratio | -0.2387 |
| max_drawdown | 0.2420 |
| cagr | -0.1044 |
| net_avg_win | 71.8363 |
| net_avg_loss | -101.9187 |
| avg_hold_time_bars | 6.6125 |
| exposure | 0.0240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
