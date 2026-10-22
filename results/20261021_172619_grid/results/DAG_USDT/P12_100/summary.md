# EMA Hourly Continuation — DAG/USDT P12_100

**Symbol:** DAG/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.8037 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9368 |
| gross_win_rate | 0.4882 |
| sharpe_ratio | -1.3536 |
| sortino_ratio | -0.4165 |
| max_drawdown | 0.4748 |
| cagr | -0.1763 |
| net_avg_win | 69.5278 |
| net_avg_loss | -82.5131 |
| avg_hold_time_bars | 21.7204 |
| exposure | 0.4591 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
