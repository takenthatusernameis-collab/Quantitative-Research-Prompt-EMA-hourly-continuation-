# EMA Hourly Continuation — ETN/USDT P20_50

**Symbol:** ETN/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 893 |
| net_profit_factor | 0.3180 |
| net_win_rate | 0.3505 |
| gross_profit_factor | 0.5178 |
| gross_win_rate | 0.3662 |
| sharpe_ratio | -11.6223 |
| sortino_ratio | -5.3705 |
| max_drawdown | 0.9967 |
| cagr | -0.9334 |
| net_avg_win | 14.8486 |
| net_avg_loss | -25.1965 |
| avg_hold_time_bars | 4.9586 |
| exposure | 0.2405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
