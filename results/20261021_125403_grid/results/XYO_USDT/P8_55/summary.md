# EMA Hourly Continuation — XYO/USDT P8_55

**Symbol:** XYO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 749 |
| net_profit_factor | 0.6078 |
| net_win_rate | 0.4299 |
| gross_profit_factor | 0.7928 |
| gross_win_rate | 0.4299 |
| sharpe_ratio | -4.9251 |
| sortino_ratio | -1.9052 |
| max_drawdown | 0.8948 |
| cagr | -0.5849 |
| net_avg_win | 42.8992 |
| net_avg_loss | -53.2212 |
| avg_hold_time_bars | 12.4085 |
| exposure | 0.4206 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
