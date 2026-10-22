# EMA Hourly Continuation — TAIKO/USDT P12_26

**Symbol:** TAIKO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.8385 |
| net_win_rate | 0.5508 |
| gross_profit_factor | 1.2144 |
| gross_win_rate | 0.5508 |
| sharpe_ratio | -1.2279 |
| sortino_ratio | -0.3976 |
| max_drawdown | 0.4492 |
| cagr | -0.1679 |
| net_avg_win | 70.6780 |
| net_avg_loss | -103.3722 |
| avg_hold_time_bars | 5.9915 |
| exposure | 0.1358 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
