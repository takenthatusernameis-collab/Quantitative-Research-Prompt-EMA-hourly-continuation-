# EMA Hourly Continuation — ETH/USDT P8_50

**Symbol:** ETH/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.6410 |
| net_win_rate | 0.4823 |
| gross_profit_factor | 0.9137 |
| gross_win_rate | 0.4823 |
| sharpe_ratio | -3.1746 |
| sortino_ratio | -1.0798 |
| max_drawdown | 0.7142 |
| cagr | -0.3906 |
| net_avg_win | 46.5519 |
| net_avg_loss | -67.6630 |
| avg_hold_time_bars | 16.7032 |
| exposure | 0.4297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
