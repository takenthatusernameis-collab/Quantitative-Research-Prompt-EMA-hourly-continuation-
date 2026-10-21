# EMA Hourly Continuation — MAGIC/USDT P20_55

**Symbol:** MAGIC/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.7492 |
| net_win_rate | 0.4927 |
| gross_profit_factor | 1.0035 |
| gross_win_rate | 0.4927 |
| sharpe_ratio | -2.6352 |
| sortino_ratio | -0.9364 |
| max_drawdown | 0.6876 |
| cagr | -0.3495 |
| net_avg_win | 64.8815 |
| net_avg_loss | -84.1142 |
| avg_hold_time_bars | 8.7358 |
| exposure | 0.2450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
