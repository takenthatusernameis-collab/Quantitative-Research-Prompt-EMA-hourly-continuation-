# EMA Hourly Continuation — ICP/USDT P20_89

**Symbol:** ICP/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.7976 |
| net_win_rate | 0.5029 |
| gross_profit_factor | 1.0094 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -1.6358 |
| sortino_ratio | -0.5287 |
| max_drawdown | 0.4927 |
| cagr | -0.2163 |
| net_avg_win | 70.4647 |
| net_avg_loss | -89.3974 |
| avg_hold_time_bars | 15.5776 |
| exposure | 0.3604 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
