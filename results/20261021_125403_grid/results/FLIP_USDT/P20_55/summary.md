# EMA Hourly Continuation — FLIP/USDT P20_55

**Symbol:** FLIP/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.6503 |
| net_win_rate | 0.4956 |
| gross_profit_factor | 1.0022 |
| gross_win_rate | 0.5044 |
| sharpe_ratio | -2.8926 |
| sortino_ratio | -0.8728 |
| max_drawdown | 0.6489 |
| cagr | -0.3350 |
| net_avg_win | 53.2265 |
| net_avg_loss | -80.4077 |
| avg_hold_time_bars | 13.2102 |
| exposure | 0.2714 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
