# EMA Hourly Continuation — BOME/USDT P55_100

**Symbol:** BOME/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.5374 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.8444 |
| gross_win_rate | 0.4876 |
| sharpe_ratio | -3.9999 |
| sortino_ratio | -1.4250 |
| max_drawdown | 0.8341 |
| cagr | -0.4996 |
| net_avg_win | 30.9836 |
| net_avg_loss | -52.8672 |
| avg_hold_time_bars | 5.4721 |
| exposure | 0.1607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
