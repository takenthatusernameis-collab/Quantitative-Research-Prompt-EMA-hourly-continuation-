# EMA Hourly Continuation — SUPER/USDT P12_55

**Symbol:** SUPER/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1014 |
| net_profit_factor | 0.6047 |
| net_win_rate | 0.4724 |
| gross_profit_factor | 0.9362 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -5.2617 |
| sortino_ratio | -2.3623 |
| max_drawdown | 0.9432 |
| cagr | -0.6753 |
| net_avg_win | 30.0466 |
| net_avg_loss | -44.4840 |
| avg_hold_time_bars | 8.0976 |
| exposure | 0.3732 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
