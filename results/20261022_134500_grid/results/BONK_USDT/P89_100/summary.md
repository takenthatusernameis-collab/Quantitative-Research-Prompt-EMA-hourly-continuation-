# EMA Hourly Continuation — BONK/USDT P89_100

**Symbol:** BONK/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 601 |
| net_profit_factor | 0.3680 |
| net_win_rate | 0.4210 |
| gross_profit_factor | 0.8219 |
| gross_win_rate | 0.4459 |
| sharpe_ratio | -7.9433 |
| sortino_ratio | -2.7684 |
| max_drawdown | 0.9752 |
| cagr | -0.7683 |
| net_avg_win | 22.4298 |
| net_avg_loss | -44.3116 |
| avg_hold_time_bars | 2.0865 |
| exposure | 0.0570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
