# EMA Hourly Continuation — SWFTC/USDT P20_55

**Symbol:** SWFTC/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.7029 |
| net_win_rate | 0.4808 |
| gross_profit_factor | 0.9173 |
| gross_win_rate | 0.4808 |
| sharpe_ratio | -2.2597 |
| sortino_ratio | -0.6794 |
| max_drawdown | 0.5526 |
| cagr | -0.2673 |
| net_avg_win | 60.2100 |
| net_avg_loss | -79.3263 |
| avg_hold_time_bars | 9.0858 |
| exposure | 0.1830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
