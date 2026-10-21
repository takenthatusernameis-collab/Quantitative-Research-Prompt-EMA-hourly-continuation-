# EMA Hourly Continuation — XDC/USDT P20_21

**Symbol:** XDC/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 132 |
| net_profit_factor | 0.4332 |
| net_win_rate | 0.4242 |
| gross_profit_factor | 0.7177 |
| gross_win_rate | 0.4242 |
| sharpe_ratio | -2.7970 |
| sortino_ratio | -0.4617 |
| max_drawdown | 0.4209 |
| cagr | -0.1927 |
| net_avg_win | 56.7703 |
| net_avg_loss | -96.5554 |
| avg_hold_time_bars | 7.8030 |
| exposure | 0.0468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
