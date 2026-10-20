# EMA Hourly Continuation — ASTR/USDT P20_34

**Symbol:** ASTR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1026 |
| net_profit_factor | 0.3835 |
| net_win_rate | 0.4366 |
| gross_profit_factor | 0.9107 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -9.2486 |
| sortino_ratio | -4.1763 |
| max_drawdown | 0.9953 |
| cagr | -0.8806 |
| net_avg_win | 13.8209 |
| net_avg_loss | -27.9321 |
| avg_hold_time_bars | 3.4172 |
| exposure | 0.1587 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
