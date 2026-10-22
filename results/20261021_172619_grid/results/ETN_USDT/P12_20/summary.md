# EMA Hourly Continuation — ETN/USDT P12_20

**Symbol:** ETN/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.4011 |
| net_win_rate | 0.3607 |
| gross_profit_factor | 0.5452 |
| gross_win_rate | 0.3607 |
| sharpe_ratio | -4.6082 |
| sortino_ratio | -1.1119 |
| max_drawdown | 0.6656 |
| cagr | -0.4062 |
| net_avg_win | 50.6459 |
| net_avg_loss | -71.2348 |
| avg_hold_time_bars | 6.3197 |
| exposure | 0.0838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
