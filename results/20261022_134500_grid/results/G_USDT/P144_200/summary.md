# EMA Hourly Continuation — G/USDT P144_200

**Symbol:** G/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.5109 |
| net_win_rate | 0.4850 |
| gross_profit_factor | 0.9742 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -3.9917 |
| sortino_ratio | -1.1134 |
| max_drawdown | 0.6881 |
| cagr | -0.4141 |
| net_avg_win | 44.2707 |
| net_avg_loss | -81.6204 |
| avg_hold_time_bars | 4.9731 |
| exposure | 0.0873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
