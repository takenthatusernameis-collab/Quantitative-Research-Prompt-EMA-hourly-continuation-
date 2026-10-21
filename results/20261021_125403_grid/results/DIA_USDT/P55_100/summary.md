# EMA Hourly Continuation — DIA/USDT P55_100

**Symbol:** DIA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.7074 |
| net_win_rate | 0.4907 |
| gross_profit_factor | 0.9662 |
| gross_win_rate | 0.4907 |
| sharpe_ratio | -2.3247 |
| sortino_ratio | -0.6873 |
| max_drawdown | 0.5741 |
| cagr | -0.2697 |
| net_avg_win | 63.0169 |
| net_avg_loss | -85.8147 |
| avg_hold_time_bars | 7.2266 |
| exposure | 0.1400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
