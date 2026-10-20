# EMA Hourly Continuation — FLIP/USDT P55_144

**Symbol:** FLIP/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.5054 |
| net_win_rate | 0.4294 |
| gross_profit_factor | 0.8536 |
| gross_win_rate | 0.4414 |
| sharpe_ratio | -4.3323 |
| sortino_ratio | -1.0995 |
| max_drawdown | 0.7584 |
| cagr | -0.4248 |
| net_avg_win | 53.6405 |
| net_avg_loss | -79.8759 |
| avg_hold_time_bars | 17.4925 |
| exposure | 0.2648 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
