# EMA Hourly Continuation — MTL/USDT P21_26

**Symbol:** MTL/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.4468 |
| net_win_rate | 0.4429 |
| gross_profit_factor | 0.8167 |
| gross_win_rate | 0.4484 |
| sharpe_ratio | -4.7726 |
| sortino_ratio | -1.3136 |
| max_drawdown | 0.7984 |
| cagr | -0.4611 |
| net_avg_win | 39.1330 |
| net_avg_loss | -69.6423 |
| avg_hold_time_bars | 5.0951 |
| exposure | 0.0848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
