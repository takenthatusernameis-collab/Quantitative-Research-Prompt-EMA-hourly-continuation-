# EMA Hourly Continuation — DOT/USDT P144_200

**Symbol:** DOT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 183 |
| net_profit_factor | 0.6825 |
| net_win_rate | 0.4973 |
| gross_profit_factor | 0.9738 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -1.5459 |
| sortino_ratio | -0.3006 |
| max_drawdown | 0.3148 |
| cagr | -0.1290 |
| net_avg_win | 69.2619 |
| net_avg_loss | -100.3738 |
| avg_hold_time_bars | 6.0109 |
| exposure | 0.0500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
