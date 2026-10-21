# EMA Hourly Continuation — AR/USDT P20_34

**Symbol:** AR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.6228 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.8312 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -2.5494 |
| sortino_ratio | -0.6458 |
| max_drawdown | 0.5290 |
| cagr | -0.2563 |
| net_avg_win | 59.7313 |
| net_avg_loss | -81.3242 |
| avg_hold_time_bars | 5.4968 |
| exposure | 0.0790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
