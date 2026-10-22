# EMA Hourly Continuation — IOTA/USDT P26_200

**Symbol:** IOTA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.6720 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.9508 |
| gross_win_rate | 0.4884 |
| sharpe_ratio | -2.2680 |
| sortino_ratio | -0.5911 |
| max_drawdown | 0.5398 |
| cagr | -0.2457 |
| net_avg_win | 63.4047 |
| net_avg_loss | -85.9627 |
| avg_hold_time_bars | 38.6192 |
| exposure | 0.6039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
