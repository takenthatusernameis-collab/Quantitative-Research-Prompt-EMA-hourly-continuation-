# EMA Hourly Continuation — ETC/USDT P12_50

**Symbol:** ETC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.6701 |
| net_win_rate | 0.4817 |
| gross_profit_factor | 0.9542 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -3.4507 |
| sortino_ratio | -1.2633 |
| max_drawdown | 0.7657 |
| cagr | -0.4389 |
| net_avg_win | 49.3673 |
| net_avg_loss | -68.4604 |
| avg_hold_time_bars | 9.2156 |
| exposure | 0.2740 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
