# EMA Hourly Continuation — SHIB/USDT P21_100

**Symbol:** SHIB/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.5944 |
| net_win_rate | 0.4642 |
| gross_profit_factor | 0.9468 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -4.8045 |
| sortino_ratio | -1.7493 |
| max_drawdown | 0.8819 |
| cagr | -0.5700 |
| net_avg_win | 41.4611 |
| net_avg_loss | -60.4277 |
| avg_hold_time_bars | 12.2866 |
| exposure | 0.3742 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
