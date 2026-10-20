# EMA Hourly Continuation — RLC/USDT P20_34

**Symbol:** RLC/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1085 |
| net_profit_factor | 0.4278 |
| net_win_rate | 0.4424 |
| gross_profit_factor | 0.9139 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -9.2176 |
| sortino_ratio | -4.3105 |
| max_drawdown | 0.9957 |
| cagr | -0.8834 |
| net_avg_win | 15.5063 |
| net_avg_loss | -28.7566 |
| avg_hold_time_bars | 3.1668 |
| exposure | 0.1562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
