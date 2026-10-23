# EMA Hourly Continuation — RLC/USDT P8_20

**Symbol:** RLC/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1590 |
| net_profit_factor | 0.4466 |
| net_win_rate | 0.4484 |
| gross_profit_factor | 0.9694 |
| gross_win_rate | 0.4736 |
| sharpe_ratio | -10.6381 |
| sortino_ratio | -5.9763 |
| max_drawdown | 0.9995 |
| cagr | -0.9497 |
| net_avg_win | 11.3102 |
| net_avg_loss | -20.5914 |
| avg_hold_time_bars | 3.3447 |
| exposure | 0.2417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
