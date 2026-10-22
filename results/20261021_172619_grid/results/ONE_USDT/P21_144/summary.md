# EMA Hourly Continuation — ONE/USDT P21_144

**Symbol:** ONE/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.8524 |
| net_win_rate | 0.5014 |
| gross_profit_factor | 1.0029 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -0.9676 |
| sortino_ratio | -0.2585 |
| max_drawdown | 0.3466 |
| cagr | -0.1143 |
| net_avg_win | 86.7026 |
| net_avg_loss | -102.3057 |
| avg_hold_time_bars | 36.4183 |
| exposure | 0.5777 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
