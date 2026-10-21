# EMA Hourly Continuation — THETA/USDT P55_89

**Symbol:** THETA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.7210 |
| net_win_rate | 0.4967 |
| gross_profit_factor | 0.9666 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -1.6803 |
| sortino_ratio | -0.4204 |
| max_drawdown | 0.4061 |
| cagr | -0.1748 |
| net_avg_win | 65.5247 |
| net_avg_loss | -89.6865 |
| avg_hold_time_bars | 6.5395 |
| exposure | 0.0904 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
