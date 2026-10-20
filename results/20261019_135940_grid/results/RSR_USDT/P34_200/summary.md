# EMA Hourly Continuation — RSR/USDT P34_200

**Symbol:** RSR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.7448 |
| net_win_rate | 0.4855 |
| gross_profit_factor | 0.9601 |
| gross_win_rate | 0.4881 |
| sharpe_ratio | -1.8682 |
| sortino_ratio | -0.5157 |
| max_drawdown | 0.4555 |
| cagr | -0.2150 |
| net_avg_win | 72.2526 |
| net_avg_loss | -91.5350 |
| avg_hold_time_bars | 27.9314 |
| exposure | 0.4812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
