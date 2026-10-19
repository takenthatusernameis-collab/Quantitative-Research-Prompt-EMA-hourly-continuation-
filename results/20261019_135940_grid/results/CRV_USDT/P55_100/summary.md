# EMA Hourly Continuation — CRV/USDT P55_100

**Symbol:** CRV/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.5500 |
| net_win_rate | 0.4774 |
| gross_profit_factor | 0.9225 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -4.8559 |
| sortino_ratio | -1.8083 |
| max_drawdown | 0.8901 |
| cagr | -0.5763 |
| net_avg_win | 32.9539 |
| net_avg_loss | -54.7393 |
| avg_hold_time_bars | 4.2183 |
| exposure | 0.1317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
