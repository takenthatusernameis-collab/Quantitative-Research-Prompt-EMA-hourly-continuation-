# EMA Hourly Continuation — POL/USDT P50_200

**Symbol:** POL/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.5703 |
| net_win_rate | 0.4729 |
| gross_profit_factor | 0.8476 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -3.1796 |
| sortino_ratio | -0.9020 |
| max_drawdown | 0.6722 |
| cagr | -0.3517 |
| net_avg_win | 45.8545 |
| net_avg_loss | -72.1329 |
| avg_hold_time_bars | 21.4852 |
| exposure | 0.3965 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
