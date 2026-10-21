# EMA Hourly Continuation — EDU/USDT P50_55

**Symbol:** EDU/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 197 |
| net_profit_factor | 0.5536 |
| net_win_rate | 0.4619 |
| gross_profit_factor | 0.8173 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -2.3512 |
| sortino_ratio | -0.4711 |
| max_drawdown | 0.4515 |
| cagr | -0.1940 |
| net_avg_win | 57.1916 |
| net_avg_loss | -88.6844 |
| avg_hold_time_bars | 5.0914 |
| exposure | 0.0454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
