# EMA Hourly Continuation — ZETA/USDT P26_144

**Symbol:** ZETA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.7321 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 1.0403 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.3197 |
| sortino_ratio | -0.6666 |
| max_drawdown | 0.6457 |
| cagr | -0.2787 |
| net_avg_win | 72.7248 |
| net_avg_loss | -96.5849 |
| avg_hold_time_bars | 27.3271 |
| exposure | 0.5293 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
