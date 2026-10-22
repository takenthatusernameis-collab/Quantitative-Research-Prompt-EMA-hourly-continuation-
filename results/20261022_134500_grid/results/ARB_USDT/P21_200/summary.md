# EMA Hourly Continuation — ARB/USDT P21_200

**Symbol:** ARB/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.7600 |
| net_win_rate | 0.5032 |
| gross_profit_factor | 1.0372 |
| gross_win_rate | 0.5064 |
| sharpe_ratio | -1.6071 |
| sortino_ratio | -0.4025 |
| max_drawdown | 0.3939 |
| cagr | -0.1746 |
| net_avg_win | 76.6237 |
| net_avg_loss | -102.1123 |
| avg_hold_time_bars | 46.2930 |
| exposure | 0.6607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
