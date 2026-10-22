# EMA Hourly Continuation — PEOPLE/USDT P20_200

**Symbol:** PEOPLE/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 1.0187 |
| net_win_rate | 0.5446 |
| gross_profit_factor | 1.1876 |
| gross_win_rate | 0.5446 |
| sharpe_ratio | 0.1573 |
| sortino_ratio | 0.0396 |
| max_drawdown | 0.1809 |
| cagr | 0.0113 |
| net_avg_win | 94.6103 |
| net_avg_loss | -111.0427 |
| avg_hold_time_bars | 46.2376 |
| exposure | 0.6340 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
