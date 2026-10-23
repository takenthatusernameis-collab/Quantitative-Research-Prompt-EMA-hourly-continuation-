# EMA Hourly Continuation — TURBO/USDT P8_26

**Symbol:** TURBO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1331 |
| net_profit_factor | 0.5281 |
| net_win_rate | 0.4343 |
| gross_profit_factor | 0.8397 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -9.7163 |
| sortino_ratio | -5.4503 |
| max_drawdown | 0.9964 |
| cagr | -0.9320 |
| net_avg_win | 19.2899 |
| net_avg_loss | -28.0391 |
| avg_hold_time_bars | 3.6499 |
| exposure | 0.2650 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
