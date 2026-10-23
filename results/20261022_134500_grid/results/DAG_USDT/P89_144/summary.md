# EMA Hourly Continuation — DAG/USDT P89_144

**Symbol:** DAG/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 539 |
| net_profit_factor | 0.3924 |
| net_win_rate | 0.4007 |
| gross_profit_factor | 0.6678 |
| gross_win_rate | 0.4137 |
| sharpe_ratio | -6.5133 |
| sortino_ratio | -2.1119 |
| max_drawdown | 0.9353 |
| cagr | -0.6627 |
| net_avg_win | 27.9442 |
| net_avg_loss | -47.6261 |
| avg_hold_time_bars | 4.6345 |
| exposure | 0.1135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
