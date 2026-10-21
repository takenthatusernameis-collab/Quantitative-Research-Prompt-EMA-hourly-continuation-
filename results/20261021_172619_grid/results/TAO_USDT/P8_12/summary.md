# EMA Hourly Continuation — TAO/USDT P8_12

**Symbol:** TAO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 168 |
| net_profit_factor | 1.0168 |
| net_win_rate | 0.5774 |
| gross_profit_factor | 1.3528 |
| gross_win_rate | 0.5774 |
| sharpe_ratio | 0.1075 |
| sortino_ratio | 0.0204 |
| max_drawdown | 0.1301 |
| cagr | 0.0055 |
| net_avg_win | 86.1081 |
| net_avg_loss | -115.7014 |
| avg_hold_time_bars | 4.4702 |
| exposure | 0.0341 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
