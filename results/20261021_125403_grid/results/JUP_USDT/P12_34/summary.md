# EMA Hourly Continuation — JUP/USDT P12_34

**Symbol:** JUP/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.7176 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9152 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -2.4056 |
| sortino_ratio | -0.8350 |
| max_drawdown | 0.6369 |
| cagr | -0.3185 |
| net_avg_win | 55.1129 |
| net_avg_loss | -71.7691 |
| avg_hold_time_bars | 6.8051 |
| exposure | 0.1825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
