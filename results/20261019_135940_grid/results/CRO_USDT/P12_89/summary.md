# EMA Hourly Continuation — CRO/USDT P12_89

**Symbol:** CRO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 767 |
| net_profit_factor | 0.4636 |
| net_win_rate | 0.4511 |
| gross_profit_factor | 0.9045 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -6.1958 |
| sortino_ratio | -2.3928 |
| max_drawdown | 0.9540 |
| cagr | -0.6989 |
| net_avg_win | 23.7513 |
| net_avg_loss | -42.1077 |
| avg_hold_time_bars | 15.0352 |
| exposure | 0.5242 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
