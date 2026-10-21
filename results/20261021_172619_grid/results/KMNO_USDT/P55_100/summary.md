# EMA Hourly Continuation — KMNO/USDT P55_100

**Symbol:** KMNO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.7939 |
| net_win_rate | 0.5118 |
| gross_profit_factor | 1.0517 |
| gross_win_rate | 0.5118 |
| sharpe_ratio | -1.3923 |
| sortino_ratio | -0.3708 |
| max_drawdown | 0.3585 |
| cagr | -0.1583 |
| net_avg_win | 76.8165 |
| net_avg_loss | -101.4207 |
| avg_hold_time_bars | 8.7647 |
| exposure | 0.1376 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
