# EMA Hourly Continuation — MLK/USDT P8_144

**Symbol:** MLK/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 858 |
| net_profit_factor | 0.4212 |
| net_win_rate | 0.3660 |
| gross_profit_factor | 0.6705 |
| gross_win_rate | 0.3741 |
| sharpe_ratio | -8.7215 |
| sortino_ratio | -3.5888 |
| max_drawdown | 0.9885 |
| cagr | -0.8289 |
| net_avg_win | 22.9094 |
| net_avg_loss | -31.3917 |
| avg_hold_time_bars | 16.1200 |
| exposure | 0.6259 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
