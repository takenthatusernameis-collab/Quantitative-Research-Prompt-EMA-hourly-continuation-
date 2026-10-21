# EMA Hourly Continuation — TAO/USDT P21_50

**Symbol:** TAO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.8021 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 1.0060 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -1.5911 |
| sortino_ratio | -0.4853 |
| max_drawdown | 0.4804 |
| cagr | -0.2008 |
| net_avg_win | 77.1644 |
| net_avg_loss | -95.7829 |
| avg_hold_time_bars | 7.2318 |
| exposure | 0.1489 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
