# EMA Hourly Continuation — KAS/USDT P20_100

**Symbol:** KAS/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.5458 |
| net_win_rate | 0.4780 |
| gross_profit_factor | 0.9104 |
| gross_win_rate | 0.4879 |
| sharpe_ratio | -4.3928 |
| sortino_ratio | -1.6352 |
| max_drawdown | 0.8690 |
| cagr | -0.5473 |
| net_avg_win | 30.8718 |
| net_avg_loss | -51.7875 |
| avg_hold_time_bars | 13.1067 |
| exposure | 0.4188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
