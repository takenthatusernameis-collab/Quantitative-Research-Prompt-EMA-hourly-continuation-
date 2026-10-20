# EMA Hourly Continuation — ORDI/USDT P8_26

**Symbol:** ORDI/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1526 |
| net_profit_factor | 0.4763 |
| net_win_rate | 0.4279 |
| gross_profit_factor | 0.8253 |
| gross_win_rate | 0.4450 |
| sharpe_ratio | -9.9896 |
| sortino_ratio | -5.4853 |
| max_drawdown | 0.9989 |
| cagr | -0.9341 |
| net_avg_win | 13.9136 |
| net_avg_loss | -21.8497 |
| avg_hold_time_bars | 4.3644 |
| exposure | 0.3027 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
