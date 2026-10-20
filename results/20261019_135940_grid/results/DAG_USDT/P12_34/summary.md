# EMA Hourly Continuation — DAG/USDT P12_34

**Symbol:** DAG/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1329 |
| net_profit_factor | 0.4000 |
| net_win_rate | 0.3830 |
| gross_profit_factor | 0.6820 |
| gross_win_rate | 0.3913 |
| sharpe_ratio | -11.9894 |
| sortino_ratio | -6.1228 |
| max_drawdown | 0.9997 |
| cagr | -0.9587 |
| net_avg_win | 13.0958 |
| net_avg_loss | -20.3200 |
| avg_hold_time_bars | 3.5177 |
| exposure | 0.2125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
