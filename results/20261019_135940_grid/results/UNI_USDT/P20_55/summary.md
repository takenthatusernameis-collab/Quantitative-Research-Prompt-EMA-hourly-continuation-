# EMA Hourly Continuation — UNI/USDT P20_55

**Symbol:** UNI/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 987 |
| net_profit_factor | 0.5010 |
| net_win_rate | 0.4600 |
| gross_profit_factor | 0.9024 |
| gross_win_rate | 0.4721 |
| sharpe_ratio | -6.9265 |
| sortino_ratio | -3.0516 |
| max_drawdown | 0.9781 |
| cagr | -0.7795 |
| net_avg_win | 21.6224 |
| net_avg_loss | -36.7581 |
| avg_hold_time_bars | 5.1216 |
| exposure | 0.2298 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
