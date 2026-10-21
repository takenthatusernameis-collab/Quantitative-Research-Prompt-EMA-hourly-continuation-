# EMA Hourly Continuation — SKL/USDT P55_100

**Symbol:** SKL/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.7019 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 0.9318 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -2.0196 |
| sortino_ratio | -0.5511 |
| max_drawdown | 0.4884 |
| cagr | -0.2232 |
| net_avg_win | 62.1352 |
| net_avg_loss | -84.7111 |
| avg_hold_time_bars | 8.1429 |
| exposure | 0.1347 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
