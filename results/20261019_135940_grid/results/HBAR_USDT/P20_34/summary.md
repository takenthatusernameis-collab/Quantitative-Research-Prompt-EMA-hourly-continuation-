# EMA Hourly Continuation — HBAR/USDT P20_34

**Symbol:** HBAR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1129 |
| net_profit_factor | 0.3640 |
| net_win_rate | 0.4393 |
| gross_profit_factor | 0.8814 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -10.3471 |
| sortino_ratio | -4.9363 |
| max_drawdown | 0.9983 |
| cagr | -0.9214 |
| net_avg_win | 11.5214 |
| net_avg_loss | -24.7990 |
| avg_hold_time_bars | 2.7042 |
| exposure | 0.1388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
