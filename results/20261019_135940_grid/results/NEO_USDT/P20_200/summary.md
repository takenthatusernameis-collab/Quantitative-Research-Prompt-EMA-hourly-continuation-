# EMA Hourly Continuation — NEO/USDT P20_200

**Symbol:** NEO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.5665 |
| net_win_rate | 0.4489 |
| gross_profit_factor | 0.8181 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -3.2119 |
| sortino_ratio | -0.8427 |
| max_drawdown | 0.6477 |
| cagr | -0.3354 |
| net_avg_win | 53.0627 |
| net_avg_loss | -76.2853 |
| avg_hold_time_bars | 41.9375 |
| exposure | 0.6710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
