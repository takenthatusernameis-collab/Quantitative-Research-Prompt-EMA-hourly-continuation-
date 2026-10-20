# EMA Hourly Continuation — ATH/USDT P12_55

**Symbol:** ATH/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 951 |
| net_profit_factor | 0.6315 |
| net_win_rate | 0.4911 |
| gross_profit_factor | 0.9711 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -4.6678 |
| sortino_ratio | -2.0882 |
| max_drawdown | 0.9098 |
| cagr | -0.6348 |
| net_avg_win | 33.2689 |
| net_avg_loss | -50.8339 |
| avg_hold_time_bars | 7.8528 |
| exposure | 0.3620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
