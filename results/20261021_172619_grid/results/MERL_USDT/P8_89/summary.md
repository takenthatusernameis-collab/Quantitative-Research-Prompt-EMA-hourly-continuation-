# EMA Hourly Continuation — MERL/USDT P8_89

**Symbol:** MERL/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.9736 |
| net_win_rate | 0.5317 |
| gross_profit_factor | 1.1291 |
| gross_win_rate | 0.5317 |
| sharpe_ratio | -0.1423 |
| sortino_ratio | -0.0470 |
| max_drawdown | 0.2786 |
| cagr | -0.0304 |
| net_avg_win | 99.0747 |
| net_avg_loss | -115.5270 |
| avg_hold_time_bars | 27.4357 |
| exposure | 0.6515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
