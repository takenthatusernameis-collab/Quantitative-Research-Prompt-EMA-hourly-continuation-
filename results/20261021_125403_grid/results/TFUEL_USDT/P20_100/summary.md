# EMA Hourly Continuation — TFUEL/USDT P20_100

**Symbol:** TFUEL/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 580 |
| net_profit_factor | 0.6515 |
| net_win_rate | 0.4397 |
| gross_profit_factor | 0.8425 |
| gross_win_rate | 0.4397 |
| sharpe_ratio | -3.8356 |
| sortino_ratio | -1.3071 |
| max_drawdown | 0.7843 |
| cagr | -0.4519 |
| net_avg_win | 57.2387 |
| net_avg_loss | -68.9287 |
| avg_hold_time_bars | 14.1052 |
| exposure | 0.3702 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
