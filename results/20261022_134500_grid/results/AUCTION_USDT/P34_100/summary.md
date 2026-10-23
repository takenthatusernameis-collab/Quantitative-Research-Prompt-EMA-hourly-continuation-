# EMA Hourly Continuation — AUCTION/USDT P34_100

**Symbol:** AUCTION/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 659 |
| net_profit_factor | 0.5722 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.9370 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -4.9838 |
| sortino_ratio | -1.8062 |
| max_drawdown | 0.8905 |
| cagr | -0.5769 |
| net_avg_win | 39.2311 |
| net_avg_loss | -57.9977 |
| avg_hold_time_bars | 9.6950 |
| exposure | 0.2892 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
