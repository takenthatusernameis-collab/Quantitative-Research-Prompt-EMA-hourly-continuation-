# EMA Hourly Continuation — RUNE/USDT P12_55

**Symbol:** RUNE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.8558 |
| net_win_rate | 0.5302 |
| gross_profit_factor | 1.1366 |
| gross_win_rate | 0.5321 |
| sharpe_ratio | -1.1552 |
| sortino_ratio | -0.3834 |
| max_drawdown | 0.3860 |
| cagr | -0.1637 |
| net_avg_win | 76.3967 |
| net_avg_loss | -100.7406 |
| avg_hold_time_bars | 18.1547 |
| exposure | 0.4374 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
