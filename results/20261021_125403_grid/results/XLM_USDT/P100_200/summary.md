# EMA Hourly Continuation — XLM/USDT P100_200

**Symbol:** XLM/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.5582 |
| net_win_rate | 0.4508 |
| gross_profit_factor | 0.7899 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -2.5973 |
| sortino_ratio | -0.5791 |
| max_drawdown | 0.4944 |
| cagr | -0.2339 |
| net_avg_win | 56.0267 |
| net_avg_loss | -82.3991 |
| avg_hold_time_bars | 12.6844 |
| exposure | 0.1407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
