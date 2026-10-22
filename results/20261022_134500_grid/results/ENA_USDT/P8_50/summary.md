# EMA Hourly Continuation — ENA/USDT P8_50

**Symbol:** ENA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1080 |
| net_profit_factor | 0.6838 |
| net_win_rate | 0.4898 |
| gross_profit_factor | 0.9490 |
| gross_win_rate | 0.4944 |
| sharpe_ratio | -3.8505 |
| sortino_ratio | -1.7833 |
| max_drawdown | 0.8906 |
| cagr | -0.5720 |
| net_avg_win | 36.0261 |
| net_avg_loss | -50.5821 |
| avg_hold_time_bars | 9.0176 |
| exposure | 0.4427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
