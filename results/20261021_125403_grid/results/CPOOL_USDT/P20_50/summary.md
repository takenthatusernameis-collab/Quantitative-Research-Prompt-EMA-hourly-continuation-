# EMA Hourly Continuation — CPOOL/USDT P20_50

**Symbol:** CPOOL/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.7819 |
| net_win_rate | 0.4908 |
| gross_profit_factor | 0.9537 |
| gross_win_rate | 0.4908 |
| sharpe_ratio | -1.6989 |
| sortino_ratio | -0.5368 |
| max_drawdown | 0.4944 |
| cagr | -0.2199 |
| net_avg_win | 69.2922 |
| net_avg_loss | -85.4221 |
| avg_hold_time_bars | 7.2761 |
| exposure | 0.1617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
