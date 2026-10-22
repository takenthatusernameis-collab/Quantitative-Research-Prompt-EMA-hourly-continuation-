# EMA Hourly Continuation — UMA/USDT P55_144

**Symbol:** UMA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.7178 |
| net_win_rate | 0.4873 |
| gross_profit_factor | 0.9401 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -1.9000 |
| sortino_ratio | -0.5101 |
| max_drawdown | 0.4667 |
| cagr | -0.2080 |
| net_avg_win | 65.5591 |
| net_avg_loss | -86.7896 |
| avg_hold_time_bars | 15.1643 |
| exposure | 0.2433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
