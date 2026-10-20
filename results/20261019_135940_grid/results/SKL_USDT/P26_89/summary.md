# EMA Hourly Continuation — SKL/USDT P26_89

**Symbol:** SKL/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 694 |
| net_profit_factor | 0.6150 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.9404 |
| gross_win_rate | 0.4870 |
| sharpe_ratio | -4.0222 |
| sortino_ratio | -1.4992 |
| max_drawdown | 0.8443 |
| cagr | -0.5073 |
| net_avg_win | 40.0954 |
| net_avg_loss | -59.4518 |
| avg_hold_time_bars | 11.2046 |
| exposure | 0.3535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
