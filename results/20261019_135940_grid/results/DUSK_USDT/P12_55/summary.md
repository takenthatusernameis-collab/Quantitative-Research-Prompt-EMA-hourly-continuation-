# EMA Hourly Continuation — DUSK/USDT P12_55

**Symbol:** DUSK/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1000 |
| net_profit_factor | 0.6267 |
| net_win_rate | 0.4530 |
| gross_profit_factor | 0.9483 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -5.7394 |
| sortino_ratio | -2.5461 |
| max_drawdown | 0.9577 |
| cagr | -0.7059 |
| net_avg_win | 35.3444 |
| net_avg_loss | -46.7062 |
| avg_hold_time_bars | 8.5790 |
| exposure | 0.3900 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
