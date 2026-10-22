# EMA Hourly Continuation — KMNO/USDT P20_55

**Symbol:** KMNO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 817 |
| net_profit_factor | 0.5444 |
| net_win_rate | 0.4517 |
| gross_profit_factor | 0.8953 |
| gross_win_rate | 0.4700 |
| sharpe_ratio | -6.0035 |
| sortino_ratio | -2.4225 |
| max_drawdown | 0.9488 |
| cagr | -0.6968 |
| net_avg_win | 30.6869 |
| net_avg_loss | -46.4289 |
| avg_hold_time_bars | 6.0894 |
| exposure | 0.2297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
