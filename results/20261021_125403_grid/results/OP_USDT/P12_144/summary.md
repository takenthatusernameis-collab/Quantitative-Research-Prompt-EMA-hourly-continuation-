# EMA Hourly Continuation — OP/USDT P12_144

**Symbol:** OP/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.7617 |
| net_win_rate | 0.4698 |
| gross_profit_factor | 0.8936 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -1.5435 |
| sortino_ratio | -0.3781 |
| max_drawdown | 0.3795 |
| cagr | -0.1605 |
| net_avg_win | 81.1567 |
| net_avg_loss | -94.4082 |
| avg_hold_time_bars | 52.4799 |
| exposure | 0.7109 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
