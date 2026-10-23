# EMA Hourly Continuation — PROM/USDT P89_144

**Symbol:** PROM/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 570 |
| net_profit_factor | 0.3201 |
| net_win_rate | 0.3789 |
| gross_profit_factor | 0.6535 |
| gross_win_rate | 0.4105 |
| sharpe_ratio | -7.9202 |
| sortino_ratio | -2.6812 |
| max_drawdown | 0.9681 |
| cagr | -0.7437 |
| net_avg_win | 21.0870 |
| net_avg_loss | -40.1904 |
| avg_hold_time_bars | 5.3439 |
| exposure | 0.1385 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
