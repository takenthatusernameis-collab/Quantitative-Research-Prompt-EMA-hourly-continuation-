# EMA Hourly Continuation — LSK/USDT P100_200

**Symbol:** LSK/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.7282 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 0.9703 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -1.6792 |
| sortino_ratio | -0.4093 |
| max_drawdown | 0.4347 |
| cagr | -0.1723 |
| net_avg_win | 70.3228 |
| net_avg_loss | -94.6020 |
| avg_hold_time_bars | 14.9553 |
| exposure | 0.1978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
