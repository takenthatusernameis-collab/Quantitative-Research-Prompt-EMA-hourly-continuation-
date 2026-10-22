# EMA Hourly Continuation — MTL/USDT P50_89

**Symbol:** MTL/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.5692 |
| net_win_rate | 0.4467 |
| gross_profit_factor | 0.8251 |
| gross_win_rate | 0.4491 |
| sharpe_ratio | -3.6439 |
| sortino_ratio | -1.0411 |
| max_drawdown | 0.7026 |
| cagr | -0.3806 |
| net_avg_win | 51.4872 |
| net_avg_loss | -73.0090 |
| avg_hold_time_bars | 9.6898 |
| exposure | 0.1767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
