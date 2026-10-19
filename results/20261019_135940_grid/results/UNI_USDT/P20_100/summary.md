# EMA Hourly Continuation — UNI/USDT P20_100

**Symbol:** UNI/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.6011 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 0.9032 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -4.1221 |
| sortino_ratio | -1.4673 |
| max_drawdown | 0.8365 |
| cagr | -0.5080 |
| net_avg_win | 41.0785 |
| net_avg_loss | -61.6692 |
| avg_hold_time_bars | 14.6003 |
| exposure | 0.4267 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
