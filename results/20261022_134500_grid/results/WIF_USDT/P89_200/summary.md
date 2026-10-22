# EMA Hourly Continuation — WIF/USDT P89_200

**Symbol:** WIF/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.5841 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.8424 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -3.3020 |
| sortino_ratio | -0.9500 |
| max_drawdown | 0.6921 |
| cagr | -0.3603 |
| net_avg_win | 49.8466 |
| net_avg_loss | -72.3834 |
| avg_hold_time_bars | 9.2440 |
| exposure | 0.1740 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
