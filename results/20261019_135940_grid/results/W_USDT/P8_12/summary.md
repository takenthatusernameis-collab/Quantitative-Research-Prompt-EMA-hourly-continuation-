# EMA Hourly Continuation — W/USDT P8_12

**Symbol:** W/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1819 |
| net_profit_factor | 0.3201 |
| net_win_rate | 0.4096 |
| gross_profit_factor | 0.7860 |
| gross_win_rate | 0.4393 |
| sharpe_ratio | -14.9711 |
| sortino_ratio | -9.1086 |
| max_drawdown | 1.0000 |
| cagr | -0.9913 |
| net_avg_win | 6.3197 |
| net_avg_loss | -13.6947 |
| avg_hold_time_bars | 1.8345 |
| exposure | 0.1517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
