# EMA Hourly Continuation — ALGO/USDT P89_144

**Symbol:** ALGO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.4921 |
| net_win_rate | 0.4630 |
| gross_profit_factor | 0.8855 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -4.6080 |
| sortino_ratio | -1.3957 |
| max_drawdown | 0.8233 |
| cagr | -0.4922 |
| net_avg_win | 37.1908 |
| net_avg_loss | -65.1730 |
| avg_hold_time_bars | 5.0391 |
| exposure | 0.1054 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
