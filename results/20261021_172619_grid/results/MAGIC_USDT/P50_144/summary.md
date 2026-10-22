# EMA Hourly Continuation — MAGIC/USDT P50_144

**Symbol:** MAGIC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.7726 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9845 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -1.5634 |
| sortino_ratio | -0.4135 |
| max_drawdown | 0.4074 |
| cagr | -0.1738 |
| net_avg_win | 76.5654 |
| net_avg_loss | -96.8069 |
| avg_hold_time_bars | 19.2456 |
| exposure | 0.2992 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
