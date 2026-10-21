# EMA Hourly Continuation — ORDI/USDT P8_200

**Symbol:** ORDI/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.7827 |
| net_win_rate | 0.4710 |
| gross_profit_factor | 0.9072 |
| gross_win_rate | 0.4710 |
| sharpe_ratio | -1.4270 |
| sortino_ratio | -0.3472 |
| max_drawdown | 0.4102 |
| cagr | -0.1482 |
| net_avg_win | 86.5357 |
| net_avg_loss | -98.4307 |
| avg_hold_time_bars | 60.0546 |
| exposure | 0.7998 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
