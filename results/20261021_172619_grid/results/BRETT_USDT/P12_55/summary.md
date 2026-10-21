# EMA Hourly Continuation — BRETT/USDT P12_55

**Symbol:** BRETT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.7847 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 0.9306 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -1.8351 |
| sortino_ratio | -0.6570 |
| max_drawdown | 0.5238 |
| cagr | -0.2628 |
| net_avg_win | 64.9294 |
| net_avg_loss | -78.1486 |
| avg_hold_time_bars | 11.8874 |
| exposure | 0.3403 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
