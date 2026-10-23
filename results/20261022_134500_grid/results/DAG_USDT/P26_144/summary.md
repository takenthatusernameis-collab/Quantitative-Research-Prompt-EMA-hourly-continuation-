# EMA Hourly Continuation — DAG/USDT P26_144

**Symbol:** DAG/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.5961 |
| net_win_rate | 0.4488 |
| gross_profit_factor | 0.8244 |
| gross_win_rate | 0.4541 |
| sharpe_ratio | -3.7492 |
| sortino_ratio | -1.2558 |
| max_drawdown | 0.7836 |
| cagr | -0.4491 |
| net_avg_win | 45.1067 |
| net_avg_loss | -61.6003 |
| avg_hold_time_bars | 16.2226 |
| exposure | 0.4174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
