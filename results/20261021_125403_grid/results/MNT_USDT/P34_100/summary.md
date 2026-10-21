# EMA Hourly Continuation — MNT/USDT P34_100

**Symbol:** MNT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.6465 |
| net_win_rate | 0.4863 |
| gross_profit_factor | 0.9125 |
| gross_win_rate | 0.4863 |
| sharpe_ratio | -2.5393 |
| sortino_ratio | -0.7267 |
| max_drawdown | 0.6058 |
| cagr | -0.2843 |
| net_avg_win | 53.2946 |
| net_avg_loss | -78.0371 |
| avg_hold_time_bars | 13.5711 |
| exposure | 0.2474 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
