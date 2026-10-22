# EMA Hourly Continuation — KNC/USDT P50_100

**Symbol:** KNC/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.6257 |
| net_win_rate | 0.4689 |
| gross_profit_factor | 0.9214 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -3.5322 |
| sortino_ratio | -1.0717 |
| max_drawdown | 0.7352 |
| cagr | -0.3889 |
| net_avg_win | 56.2139 |
| net_avg_loss | -79.3225 |
| avg_hold_time_bars | 8.2489 |
| exposure | 0.1687 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
