# EMA Hourly Continuation — KAVA/USDT P8_200

**Symbol:** KAVA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.6101 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.9059 |
| gross_win_rate | 0.4678 |
| sharpe_ratio | -3.4325 |
| sortino_ratio | -0.9809 |
| max_drawdown | 0.7095 |
| cagr | -0.3800 |
| net_avg_win | 56.6718 |
| net_avg_loss | -79.3251 |
| avg_hold_time_bars | 42.3938 |
| exposure | 0.8074 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
