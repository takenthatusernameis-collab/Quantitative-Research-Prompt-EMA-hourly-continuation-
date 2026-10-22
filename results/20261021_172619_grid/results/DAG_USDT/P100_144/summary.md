# EMA Hourly Continuation — DAG/USDT P100_144

**Symbol:** DAG/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 174 |
| net_profit_factor | 0.8081 |
| net_win_rate | 0.5115 |
| gross_profit_factor | 1.0259 |
| gross_win_rate | 0.5115 |
| sharpe_ratio | -0.7995 |
| sortino_ratio | -0.1515 |
| max_drawdown | 0.1848 |
| cagr | -0.0679 |
| net_avg_win | 76.5892 |
| net_avg_loss | -99.2409 |
| avg_hold_time_bars | 7.9885 |
| exposure | 0.0632 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
