# EMA Hourly Continuation — STRK/USDT P8_21

**Symbol:** STRK/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.7744 |
| net_win_rate | 0.5064 |
| gross_profit_factor | 1.0101 |
| gross_win_rate | 0.5064 |
| sharpe_ratio | -1.7725 |
| sortino_ratio | -0.5977 |
| max_drawdown | 0.5419 |
| cagr | -0.2405 |
| net_avg_win | 61.3572 |
| net_avg_loss | -81.2734 |
| avg_hold_time_bars | 5.1053 |
| exposure | 0.1279 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
