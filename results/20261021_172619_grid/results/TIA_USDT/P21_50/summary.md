# EMA Hourly Continuation — TIA/USDT P21_50

**Symbol:** TIA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.8700 |
| net_win_rate | 0.5244 |
| gross_profit_factor | 1.0945 |
| gross_win_rate | 0.5244 |
| sharpe_ratio | -0.9453 |
| sortino_ratio | -0.3023 |
| max_drawdown | 0.4170 |
| cagr | -0.1326 |
| net_avg_win | 77.8964 |
| net_avg_loss | -98.7240 |
| avg_hold_time_bars | 7.2073 |
| exposure | 0.1612 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
