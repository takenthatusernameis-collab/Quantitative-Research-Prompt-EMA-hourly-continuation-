# EMA Hourly Continuation — ORDI/USDT P21_55

**Symbol:** ORDI/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 965 |
| net_profit_factor | 0.5660 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.9325 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -6.2632 |
| sortino_ratio | -2.7349 |
| max_drawdown | 0.9653 |
| cagr | -0.7333 |
| net_avg_win | 28.5725 |
| net_avg_loss | -42.3046 |
| avg_hold_time_bars | 4.8518 |
| exposure | 0.2128 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
