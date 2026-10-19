# EMA Hourly Continuation — CFX/USDT P8_34

**Symbol:** CFX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1336 |
| net_profit_factor | 0.4958 |
| net_win_rate | 0.4319 |
| gross_profit_factor | 0.9142 |
| gross_win_rate | 0.4521 |
| sharpe_ratio | -9.1704 |
| sortino_ratio | -4.7066 |
| max_drawdown | 0.9973 |
| cagr | -0.9031 |
| net_avg_win | 16.9953 |
| net_avg_loss | -26.0577 |
| avg_hold_time_bars | 5.7927 |
| exposure | 0.3518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
