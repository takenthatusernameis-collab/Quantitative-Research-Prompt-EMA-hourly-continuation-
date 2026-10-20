# EMA Hourly Continuation — ANYONE/USDT P26_50

**Symbol:** ANYONE/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 796 |
| net_profit_factor | 0.4421 |
| net_win_rate | 0.3807 |
| gross_profit_factor | 0.6506 |
| gross_win_rate | 0.3819 |
| sharpe_ratio | -8.1242 |
| sortino_ratio | -3.3942 |
| max_drawdown | 0.9759 |
| cagr | -0.8065 |
| net_avg_win | 25.5096 |
| net_avg_loss | -35.4657 |
| avg_hold_time_bars | 4.3480 |
| exposure | 0.1749 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
