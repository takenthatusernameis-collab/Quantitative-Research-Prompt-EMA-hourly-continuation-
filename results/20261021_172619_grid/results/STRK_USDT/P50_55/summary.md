# EMA Hourly Continuation — STRK/USDT P50_55

**Symbol:** STRK/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 80 |
| net_profit_factor | 1.1123 |
| net_win_rate | 0.6000 |
| gross_profit_factor | 1.4777 |
| gross_win_rate | 0.6000 |
| sharpe_ratio | 0.3361 |
| sortino_ratio | 0.0444 |
| max_drawdown | 0.0712 |
| cagr | 0.0175 |
| net_avg_win | 91.6347 |
| net_avg_loss | -123.5740 |
| avg_hold_time_bars | 5.5750 |
| exposure | 0.0203 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
