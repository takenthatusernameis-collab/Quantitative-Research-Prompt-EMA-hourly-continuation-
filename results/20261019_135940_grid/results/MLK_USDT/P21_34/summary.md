# EMA Hourly Continuation — MLK/USDT P21_34

**Symbol:** MLK/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1432 |
| net_profit_factor | 0.1520 |
| net_win_rate | 0.2207 |
| gross_profit_factor | 0.5262 |
| gross_win_rate | 0.2514 |
| sharpe_ratio | -20.4272 |
| sortino_ratio | -11.4956 |
| max_drawdown | 1.0000 |
| cagr | -0.9977 |
| net_avg_win | 5.6712 |
| net_avg_loss | -10.5664 |
| avg_hold_time_bars | 2.5524 |
| exposure | 0.1654 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
