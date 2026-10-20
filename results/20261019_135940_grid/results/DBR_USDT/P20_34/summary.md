# EMA Hourly Continuation — DBR/USDT P20_34

**Symbol:** DBR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 727 |
| net_profit_factor | 0.4485 |
| net_win_rate | 0.4305 |
| gross_profit_factor | 1.0522 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -9.0262 |
| sortino_ratio | -3.8668 |
| max_drawdown | 0.9805 |
| cagr | -0.8592 |
| net_avg_win | 25.4701 |
| net_avg_loss | -42.9388 |
| avg_hold_time_bars | 4.2916 |
| exposure | 0.1774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
