# EMA Hourly Continuation — GLM/USDT P100_144

**Symbol:** GLM/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 300 |
| net_profit_factor | 0.6485 |
| net_win_rate | 0.4933 |
| gross_profit_factor | 1.0080 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.4394 |
| sortino_ratio | -0.6070 |
| max_drawdown | 0.5070 |
| cagr | -0.2426 |
| net_avg_win | 62.6378 |
| net_avg_loss | -94.0419 |
| avg_hold_time_bars | 6.4133 |
| exposure | 0.0875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
