# EMA Hourly Continuation — WEMIX/USDT P20_50

**Symbol:** WEMIX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1460 |
| net_profit_factor | 0.2041 |
| net_win_rate | 0.2911 |
| gross_profit_factor | 0.4505 |
| gross_win_rate | 0.3130 |
| sharpe_ratio | -17.5011 |
| sortino_ratio | -9.7147 |
| max_drawdown | 1.0000 |
| cagr | -0.9936 |
| net_avg_win | 6.0346 |
| net_avg_loss | -12.1398 |
| avg_hold_time_bars | 4.2692 |
| exposure | 0.2833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
