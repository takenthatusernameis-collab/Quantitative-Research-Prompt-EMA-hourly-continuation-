# EMA Hourly Continuation — DAG/USDT P12_34

**Symbol:** DAG/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.6321 |
| net_win_rate | 0.4515 |
| gross_profit_factor | 0.7906 |
| gross_win_rate | 0.4515 |
| sharpe_ratio | -2.7592 |
| sortino_ratio | -0.7947 |
| max_drawdown | 0.6175 |
| cagr | -0.3059 |
| net_avg_win | 55.4496 |
| net_avg_loss | -72.1953 |
| avg_hold_time_bars | 7.3981 |
| exposure | 0.1385 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
