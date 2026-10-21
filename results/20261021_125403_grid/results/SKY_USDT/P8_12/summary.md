# EMA Hourly Continuation — SKY/USDT P8_12

**Symbol:** SKY/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.4866 |
| net_win_rate | 0.4430 |
| gross_profit_factor | 0.8006 |
| gross_win_rate | 0.4430 |
| sharpe_ratio | -4.2374 |
| sortino_ratio | -1.1632 |
| max_drawdown | 0.6735 |
| cagr | -0.4147 |
| net_avg_win | 47.8265 |
| net_avg_loss | -78.1515 |
| avg_hold_time_bars | 4.4094 |
| exposure | 0.0733 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
