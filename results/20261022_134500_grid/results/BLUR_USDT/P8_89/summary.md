# EMA Hourly Continuation — BLUR/USDT P8_89

**Symbol:** BLUR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.7196 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0889 |
| gross_win_rate | 0.5187 |
| sharpe_ratio | -2.9400 |
| sortino_ratio | -1.0681 |
| max_drawdown | 0.7466 |
| cagr | -0.4010 |
| net_avg_win | 55.2553 |
| net_avg_loss | -78.4130 |
| avg_hold_time_bars | 21.9505 |
| exposure | 0.6625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
