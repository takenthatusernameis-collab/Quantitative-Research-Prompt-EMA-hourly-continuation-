# EMA Hourly Continuation — WIN/USDT P8_21

**Symbol:** WIN/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.6851 |
| net_win_rate | 0.5133 |
| gross_profit_factor | 1.1188 |
| gross_win_rate | 0.5133 |
| sharpe_ratio | -3.0662 |
| sortino_ratio | -1.0189 |
| max_drawdown | 0.6927 |
| cagr | -0.3703 |
| net_avg_win | 55.1544 |
| net_avg_loss | -84.8908 |
| avg_hold_time_bars | 6.4924 |
| exposure | 0.1558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
