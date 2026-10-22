# EMA Hourly Continuation — ZEC/USDT P12_50

**Symbol:** ZEC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1056 |
| net_profit_factor | 0.5475 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.9340 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -5.4791 |
| sortino_ratio | -2.4977 |
| max_drawdown | 0.9529 |
| cagr | -0.7025 |
| net_avg_win | 22.9576 |
| net_avg_loss | -37.9936 |
| avg_hold_time_bars | 6.7301 |
| exposure | 0.3230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
