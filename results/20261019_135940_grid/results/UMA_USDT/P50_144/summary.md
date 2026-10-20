# EMA Hourly Continuation — UMA/USDT P50_144

**Symbol:** UMA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.6267 |
| net_win_rate | 0.4872 |
| gross_profit_factor | 0.9787 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -3.1560 |
| sortino_ratio | -1.0049 |
| max_drawdown | 0.7068 |
| cagr | -0.3785 |
| net_avg_win | 47.1841 |
| net_avg_loss | -71.5422 |
| avg_hold_time_bars | 12.5540 |
| exposure | 0.2905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
