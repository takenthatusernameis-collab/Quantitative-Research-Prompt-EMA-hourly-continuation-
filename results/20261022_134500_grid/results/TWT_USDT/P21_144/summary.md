# EMA Hourly Continuation — TWT/USDT P21_144

**Symbol:** TWT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 561 |
| net_profit_factor | 0.5808 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9292 |
| gross_win_rate | 0.4884 |
| sharpe_ratio | -3.9251 |
| sortino_ratio | -1.3023 |
| max_drawdown | 0.8149 |
| cagr | -0.4701 |
| net_avg_win | 41.0488 |
| net_avg_loss | -65.1109 |
| avg_hold_time_bars | 20.1800 |
| exposure | 0.5146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
