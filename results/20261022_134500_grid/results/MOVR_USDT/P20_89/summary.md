# EMA Hourly Continuation — MOVR/USDT P20_89

**Symbol:** MOVR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 805 |
| net_profit_factor | 0.5276 |
| net_win_rate | 0.4385 |
| gross_profit_factor | 0.8043 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -5.5125 |
| sortino_ratio | -2.1992 |
| max_drawdown | 0.9318 |
| cagr | -0.6509 |
| net_avg_win | 29.3906 |
| net_avg_loss | -43.5030 |
| avg_hold_time_bars | 10.1975 |
| exposure | 0.3731 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
