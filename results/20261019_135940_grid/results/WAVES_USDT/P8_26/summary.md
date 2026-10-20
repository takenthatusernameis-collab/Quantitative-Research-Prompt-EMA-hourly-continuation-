# EMA Hourly Continuation — WAVES/USDT P8_26

**Symbol:** WAVES/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1692 |
| net_profit_factor | 0.4303 |
| net_win_rate | 0.4184 |
| gross_profit_factor | 0.9446 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -12.7831 |
| sortino_ratio | -7.4337 |
| max_drawdown | 0.9999 |
| cagr | -0.9774 |
| net_avg_win | 10.6695 |
| net_avg_loss | -17.8387 |
| avg_hold_time_bars | 3.6962 |
| exposure | 0.2843 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
