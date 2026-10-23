# EMA Hourly Continuation — DAG/USDT P89_200

**Symbol:** DAG/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.5516 |
| net_win_rate | 0.4535 |
| gross_profit_factor | 0.8311 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -3.8140 |
| sortino_ratio | -1.1015 |
| max_drawdown | 0.7511 |
| cagr | -0.4201 |
| net_avg_win | 47.0218 |
| net_avg_loss | -70.7407 |
| avg_hold_time_bars | 9.7767 |
| exposure | 0.1911 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
