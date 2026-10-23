# EMA Hourly Continuation — SUSHI/USDT P12_50

**Symbol:** SUSHI/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1021 |
| net_profit_factor | 0.5336 |
| net_win_rate | 0.4339 |
| gross_profit_factor | 0.9199 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -7.2147 |
| sortino_ratio | -3.2115 |
| max_drawdown | 0.9819 |
| cagr | -0.7962 |
| net_avg_win | 25.3590 |
| net_avg_loss | -36.4241 |
| avg_hold_time_bars | 8.1391 |
| exposure | 0.3760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
