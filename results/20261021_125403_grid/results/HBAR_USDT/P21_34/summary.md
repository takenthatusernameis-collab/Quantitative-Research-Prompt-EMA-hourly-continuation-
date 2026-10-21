# EMA Hourly Continuation — HBAR/USDT P21_34

**Symbol:** HBAR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 0.8602 |
| net_win_rate | 0.5602 |
| gross_profit_factor | 1.2549 |
| gross_win_rate | 0.5602 |
| sharpe_ratio | -0.6650 |
| sortino_ratio | -0.1502 |
| max_drawdown | 0.2008 |
| cagr | -0.0674 |
| net_avg_win | 73.3010 |
| net_avg_loss | -108.5279 |
| avg_hold_time_bars | 5.5311 |
| exposure | 0.0606 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
