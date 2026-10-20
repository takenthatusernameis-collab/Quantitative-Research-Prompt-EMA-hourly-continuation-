# EMA Hourly Continuation — POPCAT/USDT P12_100

**Symbol:** POPCAT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 544 |
| net_profit_factor | 0.6243 |
| net_win_rate | 0.4522 |
| gross_profit_factor | 0.8405 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -3.8613 |
| sortino_ratio | -1.3606 |
| max_drawdown | 0.7623 |
| cagr | -0.4805 |
| net_avg_win | 51.1422 |
| net_avg_loss | -67.6242 |
| avg_hold_time_bars | 20.5809 |
| exposure | 0.5914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
