# EMA Hourly Continuation — CRV/USDT P8_200

**Symbol:** CRV/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.5334 |
| net_win_rate | 0.4357 |
| gross_profit_factor | 0.8186 |
| gross_win_rate | 0.4464 |
| sharpe_ratio | -3.3570 |
| sortino_ratio | -0.7828 |
| max_drawdown | 0.6426 |
| cagr | -0.3193 |
| net_avg_win | 58.0269 |
| net_avg_loss | -84.0059 |
| avg_hold_time_bars | 67.3286 |
| exposure | 0.8569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
