# EMA Hourly Continuation — DAG/USDT P50_144

**Symbol:** DAG/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.5353 |
| net_win_rate | 0.4393 |
| gross_profit_factor | 0.7789 |
| gross_win_rate | 0.4430 |
| sharpe_ratio | -4.5822 |
| sortino_ratio | -1.4835 |
| max_drawdown | 0.8392 |
| cagr | -0.5156 |
| net_avg_win | 41.0737 |
| net_avg_loss | -60.1089 |
| avg_hold_time_bars | 10.6262 |
| exposure | 0.2584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
