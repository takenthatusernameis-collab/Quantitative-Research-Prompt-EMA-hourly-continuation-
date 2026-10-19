# EMA Hourly Continuation — ETHFI/USDT P12_89

**Symbol:** ETHFI/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 751 |
| net_profit_factor | 0.5877 |
| net_win_rate | 0.4554 |
| gross_profit_factor | 0.8502 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -4.3837 |
| sortino_ratio | -1.6909 |
| max_drawdown | 0.8713 |
| cagr | -0.5521 |
| net_avg_win | 36.1282 |
| net_avg_loss | -51.4069 |
| avg_hold_time_bars | 15.6565 |
| exposure | 0.5345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
