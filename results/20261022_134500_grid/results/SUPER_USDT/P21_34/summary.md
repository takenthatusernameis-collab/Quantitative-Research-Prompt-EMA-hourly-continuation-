# EMA Hourly Continuation — SUPER/USDT P21_34

**Symbol:** SUPER/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1110 |
| net_profit_factor | 0.3902 |
| net_win_rate | 0.4324 |
| gross_profit_factor | 0.8227 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -9.3062 |
| sortino_ratio | -4.4105 |
| max_drawdown | 0.9958 |
| cagr | -0.8862 |
| net_avg_win | 13.2736 |
| net_avg_loss | -25.9186 |
| avg_hold_time_bars | 2.9126 |
| exposure | 0.1470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
