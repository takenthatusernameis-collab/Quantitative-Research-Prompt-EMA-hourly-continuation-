# EMA Hourly Continuation — DIA/USDT P26_50

**Symbol:** DIA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 909 |
| net_profit_factor | 0.4228 |
| net_win_rate | 0.4290 |
| gross_profit_factor | 0.7878 |
| gross_win_rate | 0.4433 |
| sharpe_ratio | -7.9735 |
| sortino_ratio | -3.3668 |
| max_drawdown | 0.9857 |
| cagr | -0.8132 |
| net_avg_win | 18.5101 |
| net_avg_loss | -32.8975 |
| avg_hold_time_bars | 4.4807 |
| exposure | 0.1843 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
