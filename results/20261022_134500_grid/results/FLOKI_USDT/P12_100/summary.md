# EMA Hourly Continuation — FLOKI/USDT P12_100

**Symbol:** FLOKI/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.7157 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 1.0393 |
| gross_win_rate | 0.5079 |
| sharpe_ratio | -2.8808 |
| sortino_ratio | -1.0273 |
| max_drawdown | 0.7197 |
| cagr | -0.3844 |
| net_avg_win | 55.9327 |
| net_avg_loss | -77.6614 |
| avg_hold_time_bars | 20.5849 |
| exposure | 0.5951 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
