# EMA Hourly Continuation — ZK/USDT P50_89

**Symbol:** ZK/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.6977 |
| net_win_rate | 0.4740 |
| gross_profit_factor | 0.8952 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -2.2298 |
| sortino_ratio | -0.6295 |
| max_drawdown | 0.4969 |
| cagr | -0.2514 |
| net_avg_win | 65.6797 |
| net_avg_loss | -84.8188 |
| avg_hold_time_bars | 7.5918 |
| exposure | 0.1351 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
