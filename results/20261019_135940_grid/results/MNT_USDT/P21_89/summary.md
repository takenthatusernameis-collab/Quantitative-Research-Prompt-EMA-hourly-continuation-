# EMA Hourly Continuation — MNT/USDT P21_89

**Symbol:** MNT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.4828 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 0.8732 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -5.6432 |
| sortino_ratio | -2.0316 |
| max_drawdown | 0.9280 |
| cagr | -0.6396 |
| net_avg_win | 28.5242 |
| net_avg_loss | -49.1563 |
| avg_hold_time_bars | 13.0511 |
| exposure | 0.3945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
