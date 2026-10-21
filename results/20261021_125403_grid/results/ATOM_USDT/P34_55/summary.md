# EMA Hourly Continuation — ATOM/USDT P34_55

**Symbol:** ATOM/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.7303 |
| net_win_rate | 0.5213 |
| gross_profit_factor | 1.0707 |
| gross_win_rate | 0.5213 |
| sharpe_ratio | -1.5457 |
| sortino_ratio | -0.3750 |
| max_drawdown | 0.3578 |
| cagr | -0.1569 |
| net_avg_win | 64.2022 |
| net_avg_loss | -95.7274 |
| avg_hold_time_bars | 5.4681 |
| exposure | 0.0701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
