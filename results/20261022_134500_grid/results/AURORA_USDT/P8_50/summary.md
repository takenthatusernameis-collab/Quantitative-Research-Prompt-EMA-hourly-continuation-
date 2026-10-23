# EMA Hourly Continuation — AURORA/USDT P8_50

**Symbol:** AURORA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 956 |
| net_profit_factor | 0.5483 |
| net_win_rate | 0.4184 |
| gross_profit_factor | 0.9133 |
| gross_win_rate | 0.4320 |
| sharpe_ratio | -7.7897 |
| sortino_ratio | -3.3814 |
| max_drawdown | 0.9862 |
| cagr | -0.8111 |
| net_avg_win | 29.8875 |
| net_avg_loss | -39.2136 |
| avg_hold_time_bars | 10.7280 |
| exposure | 0.4662 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
