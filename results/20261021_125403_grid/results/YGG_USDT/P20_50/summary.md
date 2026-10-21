# EMA Hourly Continuation — YGG/USDT P20_50

**Symbol:** YGG/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.7338 |
| net_win_rate | 0.4826 |
| gross_profit_factor | 0.9504 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -2.5064 |
| sortino_ratio | -0.8343 |
| max_drawdown | 0.6327 |
| cagr | -0.3180 |
| net_avg_win | 64.9038 |
| net_avg_loss | -82.4864 |
| avg_hold_time_bars | 7.3578 |
| exposure | 0.1815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
