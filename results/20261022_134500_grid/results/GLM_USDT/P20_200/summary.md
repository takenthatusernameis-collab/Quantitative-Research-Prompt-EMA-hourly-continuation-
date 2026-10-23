# EMA Hourly Continuation — GLM/USDT P20_200

**Symbol:** GLM/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.6000 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.8505 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -3.2452 |
| sortino_ratio | -0.9626 |
| max_drawdown | 0.6838 |
| cagr | -0.3640 |
| net_avg_win | 50.6790 |
| net_avg_loss | -71.6333 |
| avg_hold_time_bars | 31.2580 |
| exposure | 0.6223 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
