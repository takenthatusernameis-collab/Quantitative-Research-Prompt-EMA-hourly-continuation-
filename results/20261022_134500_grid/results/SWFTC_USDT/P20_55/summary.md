# EMA Hourly Continuation — SWFTC/USDT P20_55

**Symbol:** SWFTC/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 929 |
| net_profit_factor | 0.3817 |
| net_win_rate | 0.4015 |
| gross_profit_factor | 0.7011 |
| gross_win_rate | 0.4166 |
| sharpe_ratio | -8.9978 |
| sortino_ratio | -3.8559 |
| max_drawdown | 0.9927 |
| cagr | -0.8584 |
| net_avg_win | 16.4319 |
| net_avg_loss | -28.8764 |
| avg_hold_time_bars | 5.2949 |
| exposure | 0.2236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
