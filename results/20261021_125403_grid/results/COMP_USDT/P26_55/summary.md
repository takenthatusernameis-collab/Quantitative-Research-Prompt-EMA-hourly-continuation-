# EMA Hourly Continuation — COMP/USDT P26_55

**Symbol:** COMP/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.6427 |
| net_win_rate | 0.4951 |
| gross_profit_factor | 0.9335 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -2.9116 |
| sortino_ratio | -0.9474 |
| max_drawdown | 0.7080 |
| cagr | -0.3524 |
| net_avg_win | 46.8612 |
| net_avg_loss | -71.5054 |
| avg_hold_time_bars | 7.9320 |
| exposure | 0.1857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
