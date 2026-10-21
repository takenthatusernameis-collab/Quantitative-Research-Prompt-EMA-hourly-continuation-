# EMA Hourly Continuation — SKY/USDT P50_100

**Symbol:** SKY/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.8462 |
| net_win_rate | 0.5438 |
| gross_profit_factor | 1.1820 |
| gross_win_rate | 0.5438 |
| sharpe_ratio | -1.0369 |
| sortino_ratio | -0.3022 |
| max_drawdown | 0.3351 |
| cagr | -0.1309 |
| net_avg_win | 76.3331 |
| net_avg_loss | -107.5306 |
| avg_hold_time_bars | 8.7221 |
| exposure | 0.1610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
