# EMA Hourly Continuation — T/USDT P12_50

**Symbol:** T/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 844 |
| net_profit_factor | 0.5397 |
| net_win_rate | 0.4562 |
| gross_profit_factor | 0.9233 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -5.8496 |
| sortino_ratio | -2.3791 |
| max_drawdown | 0.9470 |
| cagr | -0.6862 |
| net_avg_win | 28.8126 |
| net_avg_loss | -44.7834 |
| avg_hold_time_bars | 9.4017 |
| exposure | 0.3591 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
