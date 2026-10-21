# EMA Hourly Continuation — SYN/USDT P21_34

**Symbol:** SYN/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.6401 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.8758 |
| gross_win_rate | 0.4637 |
| sharpe_ratio | -2.8771 |
| sortino_ratio | -0.8206 |
| max_drawdown | 0.6235 |
| cagr | -0.3136 |
| net_avg_win | 58.7710 |
| net_avg_loss | -79.3732 |
| avg_hold_time_bars | 4.9348 |
| exposure | 0.0895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
