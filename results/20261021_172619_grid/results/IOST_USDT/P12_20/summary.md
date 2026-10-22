# EMA Hourly Continuation — IOST/USDT P12_20

**Symbol:** IOST/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.6564 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 1.0638 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -3.4508 |
| sortino_ratio | -1.1098 |
| max_drawdown | 0.7262 |
| cagr | -0.3985 |
| net_avg_win | 55.5294 |
| net_avg_loss | -83.9236 |
| avg_hold_time_bars | 5.3253 |
| exposure | 0.1205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
