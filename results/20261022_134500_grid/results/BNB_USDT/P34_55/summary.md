# EMA Hourly Continuation — BNB/USDT P34_55

**Symbol:** BNB/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 897 |
| net_profit_factor | 0.1794 |
| net_win_rate | 0.3534 |
| gross_profit_factor | 0.7815 |
| gross_win_rate | 0.4560 |
| sharpe_ratio | -13.1527 |
| sortino_ratio | -5.8287 |
| max_drawdown | 0.9996 |
| cagr | -0.9565 |
| net_avg_win | 6.8920 |
| net_avg_loss | -21.0016 |
| avg_hold_time_bars | 2.9320 |
| exposure | 0.1195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
