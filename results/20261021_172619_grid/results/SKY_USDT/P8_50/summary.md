# EMA Hourly Continuation — SKY/USDT P8_50

**Symbol:** SKY/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.7123 |
| net_win_rate | 0.4862 |
| gross_profit_factor | 0.9486 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -3.1159 |
| sortino_ratio | -1.2567 |
| max_drawdown | 0.7396 |
| cagr | -0.4390 |
| net_avg_win | 54.3471 |
| net_avg_loss | -72.1893 |
| avg_hold_time_bars | 10.8723 |
| exposure | 0.3941 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
