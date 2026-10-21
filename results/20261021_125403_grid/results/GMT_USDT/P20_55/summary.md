# EMA Hourly Continuation — GMT/USDT P20_55

**Symbol:** GMT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.7107 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9465 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -2.3856 |
| sortino_ratio | -0.7749 |
| max_drawdown | 0.6122 |
| cagr | -0.2987 |
| net_avg_win | 57.7188 |
| net_avg_loss | -77.2145 |
| avg_hold_time_bars | 8.6058 |
| exposure | 0.2015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
