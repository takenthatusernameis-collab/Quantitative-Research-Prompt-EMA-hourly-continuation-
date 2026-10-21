# EMA Hourly Continuation — ANKR/USDT P21_89

**Symbol:** ANKR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.6417 |
| net_win_rate | 0.4489 |
| gross_profit_factor | 0.8375 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -3.4766 |
| sortino_ratio | -1.1251 |
| max_drawdown | 0.7367 |
| cagr | -0.4050 |
| net_avg_win | 55.9998 |
| net_avg_loss | -71.0931 |
| avg_hold_time_bars | 17.3911 |
| exposure | 0.4103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
