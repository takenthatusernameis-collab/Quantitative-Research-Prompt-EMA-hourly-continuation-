# EMA Hourly Continuation — MASK/USDT P89_200

**Symbol:** MASK/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.6454 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9095 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -2.3377 |
| sortino_ratio | -0.5971 |
| max_drawdown | 0.5181 |
| cagr | -0.2406 |
| net_avg_win | 58.9847 |
| net_avg_loss | -84.7815 |
| avg_hold_time_bars | 14.3187 |
| exposure | 0.2083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
