# EMA Hourly Continuation — ETC/USDT P50_89

**Symbol:** ETC/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.6592 |
| net_win_rate | 0.5075 |
| gross_profit_factor | 0.9963 |
| gross_win_rate | 0.5075 |
| sharpe_ratio | -2.1606 |
| sortino_ratio | -0.5680 |
| max_drawdown | 0.4875 |
| cagr | -0.2279 |
| net_avg_win | 54.6710 |
| net_avg_loss | -85.4692 |
| avg_hold_time_bars | 8.2342 |
| exposure | 0.1246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
