# EMA Hourly Continuation — ARB/USDT P20_100

**Symbol:** ARB/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.6513 |
| net_win_rate | 0.4976 |
| gross_profit_factor | 0.9908 |
| gross_win_rate | 0.5055 |
| sharpe_ratio | -3.0596 |
| sortino_ratio | -1.0924 |
| max_drawdown | 0.7335 |
| cagr | -0.4016 |
| net_avg_win | 43.0996 |
| net_avg_loss | -65.5512 |
| avg_hold_time_bars | 15.6894 |
| exposure | 0.4500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
