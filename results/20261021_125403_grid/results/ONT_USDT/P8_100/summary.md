# EMA Hourly Continuation — ONT/USDT P8_100

**Symbol:** ONT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.7289 |
| net_win_rate | 0.4728 |
| gross_profit_factor | 0.8958 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -2.3061 |
| sortino_ratio | -0.7558 |
| max_drawdown | 0.5983 |
| cagr | -0.2943 |
| net_avg_win | 62.3996 |
| net_avg_loss | -76.7781 |
| avg_hold_time_bars | 25.8030 |
| exposure | 0.6223 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
