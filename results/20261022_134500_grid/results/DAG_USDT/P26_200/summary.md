# EMA Hourly Continuation — DAG/USDT P26_200

**Symbol:** DAG/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.6510 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.8735 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -2.8061 |
| sortino_ratio | -0.8416 |
| max_drawdown | 0.6527 |
| cagr | -0.3322 |
| net_avg_win | 55.5365 |
| net_avg_loss | -75.1301 |
| avg_hold_time_bars | 24.0525 |
| exposure | 0.4996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
