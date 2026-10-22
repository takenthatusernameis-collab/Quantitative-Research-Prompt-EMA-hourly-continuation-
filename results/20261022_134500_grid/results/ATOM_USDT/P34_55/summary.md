# EMA Hourly Continuation — ATOM/USDT P34_55

**Symbol:** ATOM/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 840 |
| net_profit_factor | 0.3303 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.8219 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -8.1815 |
| sortino_ratio | -3.3825 |
| max_drawdown | 0.9857 |
| cagr | -0.8133 |
| net_avg_win | 12.8521 |
| net_avg_loss | -31.8405 |
| avg_hold_time_bars | 3.0107 |
| exposure | 0.1150 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
