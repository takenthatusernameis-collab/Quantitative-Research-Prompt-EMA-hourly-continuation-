# EMA Hourly Continuation — AERO/USDT P34_55

**Symbol:** AERO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.7804 |
| net_win_rate | 0.5106 |
| gross_profit_factor | 1.0219 |
| gross_win_rate | 0.5106 |
| sharpe_ratio | -1.2119 |
| sortino_ratio | -0.2935 |
| max_drawdown | 0.2953 |
| cagr | -0.1268 |
| net_avg_win | 70.7228 |
| net_avg_loss | -94.5373 |
| avg_hold_time_bars | 6.0141 |
| exposure | 0.0776 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
