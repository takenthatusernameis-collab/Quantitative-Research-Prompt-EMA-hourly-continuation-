# EMA Hourly Continuation — BONK/USDT P50_55

**Symbol:** BONK/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 100 |
| net_profit_factor | 0.8558 |
| net_win_rate | 0.5300 |
| gross_profit_factor | 1.1250 |
| gross_win_rate | 0.5300 |
| sharpe_ratio | -0.4878 |
| sortino_ratio | -0.0704 |
| max_drawdown | 0.1764 |
| cagr | -0.0325 |
| net_avg_win | 89.1865 |
| net_avg_loss | -117.5117 |
| avg_hold_time_bars | 5.2500 |
| exposure | 0.0239 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
