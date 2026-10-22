# EMA Hourly Continuation — HBAR/USDT P8_20

**Symbol:** HBAR/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1772 |
| net_profit_factor | 0.3090 |
| net_win_rate | 0.4486 |
| gross_profit_factor | 0.7854 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -12.5970 |
| sortino_ratio | -7.4694 |
| max_drawdown | 0.9999 |
| cagr | -0.9790 |
| net_avg_win | 5.6245 |
| net_avg_loss | -14.8115 |
| avg_hold_time_bars | 2.5790 |
| exposure | 0.2077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
