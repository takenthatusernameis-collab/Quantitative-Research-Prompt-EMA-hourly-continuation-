# EMA Hourly Continuation — AKT/USDT P21_34

**Symbol:** AKT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1074 |
| net_profit_factor | 0.3980 |
| net_win_rate | 0.4171 |
| gross_profit_factor | 0.8569 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -9.8779 |
| sortino_ratio | -4.6000 |
| max_drawdown | 0.9969 |
| cagr | -0.8995 |
| net_avg_win | 14.7142 |
| net_avg_loss | -26.4549 |
| avg_hold_time_bars | 2.6518 |
| exposure | 0.1295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
