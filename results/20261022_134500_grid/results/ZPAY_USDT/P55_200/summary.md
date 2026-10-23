# EMA Hourly Continuation — ZPAY/USDT P55_200

**Symbol:** ZPAY/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.5676 |
| net_win_rate | 0.4069 |
| gross_profit_factor | 0.7045 |
| gross_win_rate | 0.4119 |
| sharpe_ratio | -3.4271 |
| sortino_ratio | -0.9623 |
| max_drawdown | 0.6826 |
| cagr | -0.3600 |
| net_avg_win | 54.0678 |
| net_avg_loss | -65.3676 |
| avg_hold_time_bars | 25.9603 |
| exposure | 0.4734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
