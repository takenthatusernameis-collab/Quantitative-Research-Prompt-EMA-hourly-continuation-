# EMA Hourly Continuation — RLC/USDT P8_20

**Symbol:** RLC/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.7147 |
| net_win_rate | 0.5063 |
| gross_profit_factor | 1.0383 |
| gross_win_rate | 0.5077 |
| sharpe_ratio | -2.9921 |
| sortino_ratio | -1.1515 |
| max_drawdown | 0.7573 |
| cagr | -0.4076 |
| net_avg_win | 50.6149 |
| net_avg_loss | -72.6268 |
| avg_hold_time_bars | 5.2056 |
| exposure | 0.1692 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
