# EMA Hourly Continuation — NYM/USDT P12_20

**Symbol:** NYM/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1332 |
| net_profit_factor | 0.1271 |
| net_win_rate | 0.2523 |
| gross_profit_factor | 0.4828 |
| gross_win_rate | 0.3296 |
| sharpe_ratio | -20.3740 |
| sortino_ratio | -11.4619 |
| max_drawdown | 1.0000 |
| cagr | -0.9986 |
| net_avg_win | 4.3345 |
| net_avg_loss | -11.5024 |
| avg_hold_time_bars | 3.8033 |
| exposure | 0.2303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
