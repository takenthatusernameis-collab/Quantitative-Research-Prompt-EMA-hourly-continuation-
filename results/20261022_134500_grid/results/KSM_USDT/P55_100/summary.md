# EMA Hourly Continuation — KSM/USDT P55_100

**Symbol:** KSM/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.4541 |
| net_win_rate | 0.4435 |
| gross_profit_factor | 0.8372 |
| gross_win_rate | 0.4550 |
| sharpe_ratio | -6.0810 |
| sortino_ratio | -2.1269 |
| max_drawdown | 0.9277 |
| cagr | -0.6462 |
| net_avg_win | 28.4403 |
| net_avg_loss | -49.9157 |
| avg_hold_time_bars | 5.2700 |
| exposure | 0.1464 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
