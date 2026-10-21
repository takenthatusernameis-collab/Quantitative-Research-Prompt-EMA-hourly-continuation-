# EMA Hourly Continuation — LDO/USDT P26_100

**Symbol:** LDO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.7218 |
| net_win_rate | 0.4722 |
| gross_profit_factor | 0.8772 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -2.1019 |
| sortino_ratio | -0.6332 |
| max_drawdown | 0.5319 |
| cagr | -0.2529 |
| net_avg_win | 63.5408 |
| net_avg_loss | -78.7420 |
| avg_hold_time_bars | 17.3252 |
| exposure | 0.3536 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
