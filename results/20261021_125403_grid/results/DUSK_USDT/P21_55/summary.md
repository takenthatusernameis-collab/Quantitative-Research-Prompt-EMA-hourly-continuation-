# EMA Hourly Continuation — DUSK/USDT P21_55

**Symbol:** DUSK/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.7305 |
| net_win_rate | 0.4740 |
| gross_profit_factor | 0.9297 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -2.5225 |
| sortino_ratio | -0.8342 |
| max_drawdown | 0.6775 |
| cagr | -0.3189 |
| net_avg_win | 65.7652 |
| net_avg_loss | -81.1227 |
| avg_hold_time_bars | 7.8699 |
| exposure | 0.1925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
