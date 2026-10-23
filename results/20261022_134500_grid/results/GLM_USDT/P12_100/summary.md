# EMA Hourly Continuation — GLM/USDT P12_100

**Symbol:** GLM/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.5762 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.8886 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -4.0877 |
| sortino_ratio | -1.4604 |
| max_drawdown | 0.8336 |
| cagr | -0.5009 |
| net_avg_win | 37.1597 |
| net_avg_loss | -57.1158 |
| avg_hold_time_bars | 19.9829 |
| exposure | 0.5840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
