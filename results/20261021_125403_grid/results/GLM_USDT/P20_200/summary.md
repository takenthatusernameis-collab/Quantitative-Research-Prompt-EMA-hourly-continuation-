# EMA Hourly Continuation — GLM/USDT P20_200

**Symbol:** GLM/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.7373 |
| net_win_rate | 0.4848 |
| gross_profit_factor | 0.9367 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -1.7924 |
| sortino_ratio | -0.4854 |
| max_drawdown | 0.4399 |
| cagr | -0.2014 |
| net_avg_win | 69.1999 |
| net_avg_loss | -88.3079 |
| avg_hold_time_bars | 37.4321 |
| exposure | 0.6142 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
