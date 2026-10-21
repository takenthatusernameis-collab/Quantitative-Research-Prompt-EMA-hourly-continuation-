# EMA Hourly Continuation — BTC/USDT P55_100

**Symbol:** BTC/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.5501 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 1.0275 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -3.3400 |
| sortino_ratio | -0.8340 |
| max_drawdown | 0.6669 |
| cagr | -0.3162 |
| net_avg_win | 48.1918 |
| net_avg_loss | -86.5680 |
| avg_hold_time_bars | 8.5828 |
| exposure | 0.1160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
