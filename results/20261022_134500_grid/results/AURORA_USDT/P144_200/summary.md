# EMA Hourly Continuation — AURORA/USDT P144_200

**Symbol:** AURORA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.6158 |
| net_win_rate | 0.5168 |
| gross_profit_factor | 1.1720 |
| gross_win_rate | 0.5352 |
| sharpe_ratio | -2.7620 |
| sortino_ratio | -0.7113 |
| max_drawdown | 0.5846 |
| cagr | -0.2873 |
| net_avg_win | 54.3342 |
| net_avg_loss | -94.3760 |
| avg_hold_time_bars | 4.8257 |
| exposure | 0.0717 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
