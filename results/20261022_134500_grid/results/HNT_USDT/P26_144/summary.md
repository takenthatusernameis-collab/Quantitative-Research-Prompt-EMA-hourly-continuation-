# EMA Hourly Continuation — HNT/USDT P26_144

**Symbol:** HNT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.5641 |
| net_win_rate | 0.4259 |
| gross_profit_factor | 0.7630 |
| gross_win_rate | 0.4296 |
| sharpe_ratio | -4.4229 |
| sortino_ratio | -1.4391 |
| max_drawdown | 0.8321 |
| cagr | -0.4989 |
| net_avg_win | 46.3334 |
| net_avg_loss | -60.9439 |
| avg_hold_time_bars | 19.2556 |
| exposure | 0.4726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
