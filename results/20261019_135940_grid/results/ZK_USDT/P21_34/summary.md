# EMA Hourly Continuation — ZK/USDT P21_34

**Symbol:** ZK/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1101 |
| net_profit_factor | 0.4999 |
| net_win_rate | 0.4305 |
| gross_profit_factor | 0.9805 |
| gross_win_rate | 0.4496 |
| sharpe_ratio | -9.5145 |
| sortino_ratio | -4.6132 |
| max_drawdown | 0.9956 |
| cagr | -0.9010 |
| net_avg_win | 20.9920 |
| net_avg_loss | -31.7475 |
| avg_hold_time_bars | 2.6894 |
| exposure | 0.1444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
