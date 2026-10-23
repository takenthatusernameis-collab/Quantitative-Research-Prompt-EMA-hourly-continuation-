# EMA Hourly Continuation — GLM/USDT P12_55

**Symbol:** GLM/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 953 |
| net_profit_factor | 0.4604 |
| net_win_rate | 0.4502 |
| gross_profit_factor | 0.8001 |
| gross_win_rate | 0.4638 |
| sharpe_ratio | -6.5059 |
| sortino_ratio | -2.8353 |
| max_drawdown | 0.9684 |
| cagr | -0.7436 |
| net_avg_win | 19.2347 |
| net_avg_loss | -34.2056 |
| avg_hold_time_bars | 9.4827 |
| exposure | 0.4108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
