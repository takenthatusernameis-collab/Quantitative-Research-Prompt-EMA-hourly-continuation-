# EMA Hourly Continuation — KAS/USDT P21_89

**Symbol:** KAS/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.8176 |
| net_win_rate | 0.5114 |
| gross_profit_factor | 1.0310 |
| gross_win_rate | 0.5114 |
| sharpe_ratio | -1.3129 |
| sortino_ratio | -0.4137 |
| max_drawdown | 0.4014 |
| cagr | -0.1743 |
| net_avg_win | 69.5863 |
| net_avg_loss | -89.0916 |
| avg_hold_time_bars | 14.7339 |
| exposure | 0.3221 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
