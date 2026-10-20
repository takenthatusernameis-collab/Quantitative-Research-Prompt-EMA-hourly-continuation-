# EMA Hourly Continuation — DIA/USDT P50_200

**Symbol:** DIA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.6376 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 0.9513 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -2.6915 |
| sortino_ratio | -0.7545 |
| max_drawdown | 0.6369 |
| cagr | -0.3060 |
| net_avg_win | 54.5907 |
| net_avg_loss | -80.2445 |
| avg_hold_time_bars | 21.8554 |
| exposure | 0.3966 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
