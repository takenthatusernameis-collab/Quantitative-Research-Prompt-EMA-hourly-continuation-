# EMA Hourly Continuation — AAVE/USDT P12_50

**Symbol:** AAVE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1056 |
| net_profit_factor | 0.5672 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.9313 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -7.1464 |
| sortino_ratio | -3.2704 |
| max_drawdown | 0.9819 |
| cagr | -0.7947 |
| net_avg_win | 27.1899 |
| net_avg_loss | -38.8906 |
| avg_hold_time_bars | 7.2121 |
| exposure | 0.3462 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
