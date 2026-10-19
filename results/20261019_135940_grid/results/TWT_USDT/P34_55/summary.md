# EMA Hourly Continuation — TWT/USDT P34_55

**Symbol:** TWT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 955 |
| net_profit_factor | 0.3199 |
| net_win_rate | 0.4199 |
| gross_profit_factor | 0.8100 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -10.2424 |
| sortino_ratio | -4.5248 |
| max_drawdown | 0.9971 |
| cagr | -0.9010 |
| net_avg_win | 11.6921 |
| net_avg_loss | -26.4595 |
| avg_hold_time_bars | 3.1393 |
| exposure | 0.1363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
