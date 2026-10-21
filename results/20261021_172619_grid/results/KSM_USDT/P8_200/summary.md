# EMA Hourly Continuation — KSM/USDT P8_200

**Symbol:** KSM/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.7508 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.9049 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -1.6509 |
| sortino_ratio | -0.4005 |
| max_drawdown | 0.4416 |
| cagr | -0.1697 |
| net_avg_win | 81.4748 |
| net_avg_loss | -97.2442 |
| avg_hold_time_bars | 60.2260 |
| exposure | 0.7994 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
