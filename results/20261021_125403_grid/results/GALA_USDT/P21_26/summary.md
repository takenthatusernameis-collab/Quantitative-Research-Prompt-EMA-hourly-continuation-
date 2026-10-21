# EMA Hourly Continuation — GALA/USDT P21_26

**Symbol:** GALA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 157 |
| net_profit_factor | 0.5366 |
| net_win_rate | 0.4268 |
| gross_profit_factor | 0.7360 |
| gross_win_rate | 0.4268 |
| sharpe_ratio | -2.3863 |
| sortino_ratio | -0.4260 |
| max_drawdown | 0.3970 |
| cagr | -0.1787 |
| net_avg_win | 67.4301 |
| net_avg_loss | -93.5398 |
| avg_hold_time_bars | 3.9682 |
| exposure | 0.0283 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
