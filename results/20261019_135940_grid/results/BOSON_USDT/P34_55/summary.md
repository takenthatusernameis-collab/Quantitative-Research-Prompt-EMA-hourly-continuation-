# EMA Hourly Continuation — BOSON/USDT P34_55

**Symbol:** BOSON/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 849 |
| net_profit_factor | 0.4286 |
| net_win_rate | 0.4193 |
| gross_profit_factor | 0.7887 |
| gross_win_rate | 0.4382 |
| sharpe_ratio | -7.4176 |
| sortino_ratio | -3.0278 |
| max_drawdown | 0.9768 |
| cagr | -0.7765 |
| net_avg_win | 20.5782 |
| net_avg_loss | -34.6729 |
| avg_hold_time_bars | 3.8834 |
| exposure | 0.1499 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
