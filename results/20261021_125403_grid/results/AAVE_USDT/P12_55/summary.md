# EMA Hourly Continuation — AAVE/USDT P12_55

**Symbol:** AAVE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.7018 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.8854 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -2.7962 |
| sortino_ratio | -0.9467 |
| max_drawdown | 0.6800 |
| cagr | -0.3523 |
| net_avg_win | 59.4362 |
| net_avg_loss | -73.5068 |
| avg_hold_time_bars | 13.2244 |
| exposure | 0.3402 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
