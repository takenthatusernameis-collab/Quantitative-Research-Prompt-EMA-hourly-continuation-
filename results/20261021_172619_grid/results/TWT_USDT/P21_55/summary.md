# EMA Hourly Continuation — TWT/USDT P21_55

**Symbol:** TWT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 570 |
| net_profit_factor | 0.7341 |
| net_win_rate | 0.5281 |
| gross_profit_factor | 1.0806 |
| gross_win_rate | 0.5281 |
| sharpe_ratio | -2.0529 |
| sortino_ratio | -0.7084 |
| max_drawdown | 0.6038 |
| cagr | -0.2759 |
| net_avg_win | 50.9589 |
| net_avg_loss | -77.6719 |
| avg_hold_time_bars | 7.7298 |
| exposure | 0.2003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
