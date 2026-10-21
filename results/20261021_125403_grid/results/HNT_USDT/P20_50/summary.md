# EMA Hourly Continuation — HNT/USDT P20_50

**Symbol:** HNT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.7287 |
| net_win_rate | 0.4927 |
| gross_profit_factor | 0.9359 |
| gross_win_rate | 0.4927 |
| sharpe_ratio | -1.9872 |
| sortino_ratio | -0.6233 |
| max_drawdown | 0.5281 |
| cagr | -0.2488 |
| net_avg_win | 58.0790 |
| net_avg_loss | -77.4161 |
| avg_hold_time_bars | 7.9543 |
| exposure | 0.1739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
