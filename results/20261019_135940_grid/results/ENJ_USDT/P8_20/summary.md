# EMA Hourly Continuation — ENJ/USDT P8_20

**Symbol:** ENJ/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1660 |
| net_profit_factor | 0.3489 |
| net_win_rate | 0.4283 |
| gross_profit_factor | 0.8182 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -11.9536 |
| sortino_ratio | -6.8710 |
| max_drawdown | 0.9998 |
| cagr | -0.9693 |
| net_avg_win | 7.5366 |
| net_avg_loss | -16.1822 |
| avg_hold_time_bars | 2.9952 |
| exposure | 0.2260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
