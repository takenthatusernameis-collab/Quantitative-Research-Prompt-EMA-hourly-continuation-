# EMA Hourly Continuation — STRK/USDT P12_200

**Symbol:** STRK/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.7906 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 0.9266 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -1.2024 |
| sortino_ratio | -0.2868 |
| max_drawdown | 0.3230 |
| cagr | -0.1250 |
| net_avg_win | 79.1079 |
| net_avg_loss | -93.8453 |
| avg_hold_time_bars | 59.1815 |
| exposure | 0.7559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
