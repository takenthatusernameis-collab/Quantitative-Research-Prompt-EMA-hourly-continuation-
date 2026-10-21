# EMA Hourly Continuation — GTC/USDT P12_200

**Symbol:** GTC/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.7344 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.8729 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -1.8084 |
| sortino_ratio | -0.4821 |
| max_drawdown | 0.4666 |
| cagr | -0.1995 |
| net_avg_win | 71.7406 |
| net_avg_loss | -85.7398 |
| avg_hold_time_bars | 42.3513 |
| exposure | 0.6795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
