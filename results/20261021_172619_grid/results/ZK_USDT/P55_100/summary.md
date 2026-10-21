# EMA Hourly Continuation — ZK/USDT P55_100

**Symbol:** ZK/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.7573 |
| net_win_rate | 0.4901 |
| gross_profit_factor | 0.9633 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -1.7406 |
| sortino_ratio | -0.4859 |
| max_drawdown | 0.4133 |
| cagr | -0.2005 |
| net_avg_win | 73.1212 |
| net_avg_loss | -92.8228 |
| avg_hold_time_bars | 8.1859 |
| exposure | 0.1417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
