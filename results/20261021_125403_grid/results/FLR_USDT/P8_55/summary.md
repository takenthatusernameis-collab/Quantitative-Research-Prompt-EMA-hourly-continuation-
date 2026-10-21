# EMA Hourly Continuation — FLR/USDT P8_55

**Symbol:** FLR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 716 |
| net_profit_factor | 0.7464 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9897 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -2.4425 |
| sortino_ratio | -0.9368 |
| max_drawdown | 0.6839 |
| cagr | -0.3490 |
| net_avg_win | 54.2450 |
| net_avg_loss | -72.6734 |
| avg_hold_time_bars | 12.8087 |
| exposure | 0.4169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
