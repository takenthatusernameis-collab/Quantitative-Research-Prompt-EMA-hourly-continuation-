# EMA Hourly Continuation — FLUX/USDT P21_55

**Symbol:** FLUX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.6955 |
| net_win_rate | 0.4720 |
| gross_profit_factor | 0.9173 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -2.7906 |
| sortino_ratio | -0.9062 |
| max_drawdown | 0.6756 |
| cagr | -0.3392 |
| net_avg_win | 60.5410 |
| net_avg_loss | -77.7973 |
| avg_hold_time_bars | 7.2244 |
| exposure | 0.1698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
