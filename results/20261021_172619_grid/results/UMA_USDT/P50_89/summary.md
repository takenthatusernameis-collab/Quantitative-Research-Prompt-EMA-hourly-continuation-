# EMA Hourly Continuation — UMA/USDT P50_89

**Symbol:** UMA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.7446 |
| net_win_rate | 0.5134 |
| gross_profit_factor | 1.0635 |
| gross_win_rate | 0.5134 |
| sharpe_ratio | -1.9889 |
| sortino_ratio | -0.5795 |
| max_drawdown | 0.5107 |
| cagr | -0.2328 |
| net_avg_win | 67.1666 |
| net_avg_loss | -95.1615 |
| avg_hold_time_bars | 8.1800 |
| exposure | 0.1528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
