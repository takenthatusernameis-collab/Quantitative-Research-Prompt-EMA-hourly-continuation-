# EMA Hourly Continuation — MINA/USDT P8_34

**Symbol:** MINA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1365 |
| net_profit_factor | 0.4730 |
| net_win_rate | 0.4579 |
| gross_profit_factor | 0.8494 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -7.8887 |
| sortino_ratio | -4.1064 |
| max_drawdown | 0.9932 |
| cagr | -0.8631 |
| net_avg_win | 14.2657 |
| net_avg_loss | -25.4707 |
| avg_hold_time_bars | 5.6777 |
| exposure | 0.3523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
