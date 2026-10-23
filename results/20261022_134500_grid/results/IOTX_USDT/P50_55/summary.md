# EMA Hourly Continuation — IOTX/USDT P50_55

**Symbol:** IOTX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 856 |
| net_profit_factor | 0.2021 |
| net_win_rate | 0.3505 |
| gross_profit_factor | 0.6235 |
| gross_win_rate | 0.4171 |
| sharpe_ratio | -12.6391 |
| sortino_ratio | -5.4201 |
| max_drawdown | 0.9994 |
| cagr | -0.9477 |
| net_avg_win | 8.4363 |
| net_avg_loss | -22.5267 |
| avg_hold_time_bars | 2.0479 |
| exposure | 0.0797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
