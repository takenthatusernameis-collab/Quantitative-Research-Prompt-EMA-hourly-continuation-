# EMA Hourly Continuation — BCH/USDT P50_100

**Symbol:** BCH/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.5774 |
| net_win_rate | 0.4523 |
| gross_profit_factor | 0.8119 |
| gross_win_rate | 0.4523 |
| sharpe_ratio | -3.0076 |
| sortino_ratio | -0.7740 |
| max_drawdown | 0.5935 |
| cagr | -0.2988 |
| net_avg_win | 54.8400 |
| net_avg_loss | -78.4322 |
| avg_hold_time_bars | 9.8923 |
| exposure | 0.1461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
