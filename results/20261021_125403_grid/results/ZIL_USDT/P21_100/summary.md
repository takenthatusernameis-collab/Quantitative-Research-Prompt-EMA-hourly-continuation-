# EMA Hourly Continuation — ZIL/USDT P21_100

**Symbol:** ZIL/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.8069 |
| net_win_rate | 0.5087 |
| gross_profit_factor | 1.0445 |
| gross_win_rate | 0.5087 |
| sharpe_ratio | -1.5446 |
| sortino_ratio | -0.4742 |
| max_drawdown | 0.5332 |
| cagr | -0.1969 |
| net_avg_win | 75.9542 |
| net_avg_loss | -97.4724 |
| avg_hold_time_bars | 18.4869 |
| exposure | 0.3849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
