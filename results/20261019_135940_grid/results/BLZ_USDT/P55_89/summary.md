# EMA Hourly Continuation — BLZ/USDT P55_89

**Symbol:** BLZ/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 731 |
| net_profit_factor | 0.4447 |
| net_win_rate | 0.3926 |
| gross_profit_factor | 0.7978 |
| gross_win_rate | 0.4104 |
| sharpe_ratio | -8.1340 |
| sortino_ratio | -3.1007 |
| max_drawdown | 0.9801 |
| cagr | -0.7838 |
| net_avg_win | 27.3219 |
| net_avg_loss | -39.7103 |
| avg_hold_time_bars | 5.4118 |
| exposure | 0.1790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
