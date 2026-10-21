# EMA Hourly Continuation — ZEC/USDT P21_89

**Symbol:** ZEC/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.9726 |
| net_win_rate | 0.5399 |
| gross_profit_factor | 1.1630 |
| gross_win_rate | 0.5399 |
| sharpe_ratio | -0.1245 |
| sortino_ratio | -0.0372 |
| max_drawdown | 0.2868 |
| cagr | -0.0244 |
| net_avg_win | 92.8280 |
| net_avg_loss | -111.9957 |
| avg_hold_time_bars | 17.3991 |
| exposure | 0.3369 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
