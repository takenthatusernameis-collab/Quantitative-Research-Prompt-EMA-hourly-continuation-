# EMA Hourly Continuation — DAG/USDT P20_144

**Symbol:** DAG/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.7812 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9068 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -1.4398 |
| sortino_ratio | -0.4152 |
| max_drawdown | 0.4250 |
| cagr | -0.1753 |
| net_avg_win | 69.5266 |
| net_avg_loss | -82.3179 |
| avg_hold_time_bars | 24.0341 |
| exposure | 0.4479 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
