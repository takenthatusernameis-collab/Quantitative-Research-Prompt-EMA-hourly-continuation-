# EMA Hourly Continuation — METIS/USDT P21_100

**Symbol:** METIS/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.5507 |
| net_win_rate | 0.4319 |
| gross_profit_factor | 0.8151 |
| gross_win_rate | 0.4392 |
| sharpe_ratio | -5.3276 |
| sortino_ratio | -1.9542 |
| max_drawdown | 0.9071 |
| cagr | -0.6090 |
| net_avg_win | 37.6118 |
| net_avg_loss | -51.9315 |
| avg_hold_time_bars | 12.5725 |
| exposure | 0.3903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
