# EMA Hourly Continuation — CRV/USDT P21_200

**Symbol:** CRV/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.8500 |
| net_win_rate | 0.5016 |
| gross_profit_factor | 1.0091 |
| gross_win_rate | 0.5016 |
| sharpe_ratio | -0.9221 |
| sortino_ratio | -0.2312 |
| max_drawdown | 0.2890 |
| cagr | -0.1028 |
| net_avg_win | 87.7900 |
| net_avg_loss | -103.9564 |
| avg_hold_time_bars | 42.7068 |
| exposure | 0.5960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
