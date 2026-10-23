# EMA Hourly Continuation — DAG/USDT P12_144

**Symbol:** DAG/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.6069 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8561 |
| gross_win_rate | 0.4608 |
| sharpe_ratio | -3.9685 |
| sortino_ratio | -1.4065 |
| max_drawdown | 0.8207 |
| cagr | -0.4907 |
| net_avg_win | 43.4559 |
| net_avg_loss | -59.6705 |
| avg_hold_time_bars | 20.1803 |
| exposure | 0.5852 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
