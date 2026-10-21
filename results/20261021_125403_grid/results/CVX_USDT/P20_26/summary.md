# EMA Hourly Continuation — CVX/USDT P20_26

**Symbol:** CVX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 239 |
| net_profit_factor | 0.8374 |
| net_win_rate | 0.5439 |
| gross_profit_factor | 1.1825 |
| gross_win_rate | 0.5439 |
| sharpe_ratio | -0.8330 |
| sortino_ratio | -0.1867 |
| max_drawdown | 0.3229 |
| cagr | -0.0828 |
| net_avg_win | 77.2509 |
| net_avg_loss | -110.0261 |
| avg_hold_time_bars | 4.6276 |
| exposure | 0.0503 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
