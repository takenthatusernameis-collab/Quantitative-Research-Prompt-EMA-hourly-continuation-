# EMA Hourly Continuation — MLK/USDT P89_200

**Symbol:** MLK/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.4415 |
| net_win_rate | 0.3594 |
| gross_profit_factor | 0.6024 |
| gross_win_rate | 0.3594 |
| sharpe_ratio | -4.4739 |
| sortino_ratio | -1.0575 |
| max_drawdown | 0.7128 |
| cagr | -0.3902 |
| net_avg_win | 55.7971 |
| net_avg_loss | -70.9105 |
| avg_hold_time_bars | 14.3737 |
| exposure | 0.1828 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
