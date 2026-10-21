# EMA Hourly Continuation — ADA/USDT P8_100

**Symbol:** ADA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.7801 |
| net_win_rate | 0.4945 |
| gross_profit_factor | 0.9633 |
| gross_win_rate | 0.4945 |
| sharpe_ratio | -1.6014 |
| sortino_ratio | -0.4868 |
| max_drawdown | 0.4497 |
| cagr | -0.2019 |
| net_avg_win | 68.4994 |
| net_avg_loss | -85.8886 |
| avg_hold_time_bars | 30.3664 |
| exposure | 0.6253 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
