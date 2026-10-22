# EMA Hourly Continuation — DIA/USDT P26_50

**Symbol:** DIA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.6041 |
| net_win_rate | 0.4515 |
| gross_profit_factor | 0.8350 |
| gross_win_rate | 0.4515 |
| sharpe_ratio | -3.5924 |
| sortino_ratio | -1.1135 |
| max_drawdown | 0.7493 |
| cagr | -0.4002 |
| net_avg_win | 51.6737 |
| net_avg_loss | -70.4004 |
| avg_hold_time_bars | 6.8586 |
| exposure | 0.1471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
