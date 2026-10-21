# EMA Hourly Continuation — ATOM/USDT P8_89

**Symbol:** ATOM/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.8280 |
| net_win_rate | 0.5103 |
| gross_profit_factor | 1.0404 |
| gross_win_rate | 0.5103 |
| sharpe_ratio | -1.1344 |
| sortino_ratio | -0.3210 |
| max_drawdown | 0.3327 |
| cagr | -0.1383 |
| net_avg_win | 75.8112 |
| net_avg_loss | -95.4193 |
| avg_hold_time_bars | 39.6778 |
| exposure | 0.6998 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
