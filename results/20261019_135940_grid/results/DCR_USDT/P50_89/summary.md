# EMA Hourly Continuation — DCR/USDT P50_89

**Symbol:** DCR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.4256 |
| net_win_rate | 0.4253 |
| gross_profit_factor | 0.7885 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -7.0056 |
| sortino_ratio | -2.6127 |
| max_drawdown | 0.9612 |
| cagr | -0.7239 |
| net_avg_win | 23.8196 |
| net_avg_loss | -41.4178 |
| avg_hold_time_bars | 5.4865 |
| exposure | 0.1745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
