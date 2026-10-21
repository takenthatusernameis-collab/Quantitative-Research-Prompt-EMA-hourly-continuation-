# EMA Hourly Continuation — DASH/USDT P26_200

**Symbol:** DASH/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.7157 |
| net_win_rate | 0.4712 |
| gross_profit_factor | 0.8938 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -1.7372 |
| sortino_ratio | -0.4121 |
| max_drawdown | 0.4171 |
| cagr | -0.1735 |
| net_avg_win | 73.0585 |
| net_avg_loss | -90.9739 |
| avg_hold_time_bars | 43.8957 |
| exposure | 0.5547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
