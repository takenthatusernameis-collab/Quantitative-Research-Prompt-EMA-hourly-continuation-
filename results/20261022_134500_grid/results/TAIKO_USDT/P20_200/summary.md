# EMA Hourly Continuation — TAIKO/USDT P20_200

**Symbol:** TAIKO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 0.6403 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.8747 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -2.2854 |
| sortino_ratio | -0.5345 |
| max_drawdown | 0.4823 |
| cagr | -0.2231 |
| net_avg_win | 65.8392 |
| net_avg_loss | -90.2480 |
| avg_hold_time_bars | 57.0498 |
| exposure | 0.7152 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
