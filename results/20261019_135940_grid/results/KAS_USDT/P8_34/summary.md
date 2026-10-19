# EMA Hourly Continuation — KAS/USDT P8_34

**Symbol:** KAS/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1448 |
| net_profit_factor | 0.4363 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 0.8575 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -8.5097 |
| sortino_ratio | -4.5079 |
| max_drawdown | 0.9969 |
| cagr | -0.8975 |
| net_avg_win | 11.4637 |
| net_avg_loss | -22.8159 |
| avg_hold_time_bars | 5.2030 |
| exposure | 0.3425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
