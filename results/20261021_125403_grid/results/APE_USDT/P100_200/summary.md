# EMA Hourly Continuation — APE/USDT P100_200

**Symbol:** APE/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.6732 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 0.8509 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -1.8377 |
| sortino_ratio | -0.4376 |
| max_drawdown | 0.4018 |
| cagr | -0.1821 |
| net_avg_win | 62.3302 |
| net_avg_loss | -81.9513 |
| avg_hold_time_bars | 11.2903 |
| exposure | 0.1432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
