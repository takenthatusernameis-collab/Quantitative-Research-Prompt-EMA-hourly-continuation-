# EMA Hourly Continuation — JTO/USDT P21_50

**Symbol:** JTO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.7966 |
| net_win_rate | 0.5019 |
| gross_profit_factor | 1.0145 |
| gross_win_rate | 0.5019 |
| sharpe_ratio | -1.7206 |
| sortino_ratio | -0.5733 |
| max_drawdown | 0.5228 |
| cagr | -0.2328 |
| net_avg_win | 70.2282 |
| net_avg_loss | -88.8153 |
| avg_hold_time_bars | 8.1352 |
| exposure | 0.1997 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
