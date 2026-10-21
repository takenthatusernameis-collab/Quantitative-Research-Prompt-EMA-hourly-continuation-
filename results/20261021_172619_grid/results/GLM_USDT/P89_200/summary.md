# EMA Hourly Continuation — GLM/USDT P89_200

**Symbol:** GLM/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.6790 |
| net_win_rate | 0.4804 |
| gross_profit_factor | 0.9165 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -2.2306 |
| sortino_ratio | -0.5784 |
| max_drawdown | 0.5037 |
| cagr | -0.2357 |
| net_avg_win | 65.3161 |
| net_avg_loss | -88.9219 |
| avg_hold_time_bars | 13.6888 |
| exposure | 0.2060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
