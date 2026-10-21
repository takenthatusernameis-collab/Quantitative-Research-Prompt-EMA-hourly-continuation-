# EMA Hourly Continuation — POL/USDT P34_50

**Symbol:** POL/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.6073 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.8765 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -2.3267 |
| sortino_ratio | -0.5324 |
| max_drawdown | 0.4655 |
| cagr | -0.2162 |
| net_avg_win | 58.4812 |
| net_avg_loss | -86.9588 |
| avg_hold_time_bars | 5.5020 |
| exposure | 0.0638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
