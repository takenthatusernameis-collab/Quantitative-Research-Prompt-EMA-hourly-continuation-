# EMA Hourly Continuation — MEW/USDT P20_200

**Symbol:** MEW/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.7080 |
| net_win_rate | 0.4826 |
| gross_profit_factor | 0.9320 |
| gross_win_rate | 0.4853 |
| sharpe_ratio | -2.0621 |
| sortino_ratio | -0.5614 |
| max_drawdown | 0.5441 |
| cagr | -0.2339 |
| net_avg_win | 65.7041 |
| net_avg_loss | -86.5532 |
| avg_hold_time_bars | 37.8445 |
| exposure | 0.6416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
