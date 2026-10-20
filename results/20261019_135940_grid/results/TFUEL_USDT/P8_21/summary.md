# EMA Hourly Continuation — TFUEL/USDT P8_21

**Symbol:** TFUEL/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1765 |
| net_profit_factor | 0.3666 |
| net_win_rate | 0.3819 |
| gross_profit_factor | 0.7680 |
| gross_win_rate | 0.4085 |
| sharpe_ratio | -15.1349 |
| sortino_ratio | -9.0349 |
| max_drawdown | 1.0000 |
| cagr | -0.9901 |
| net_avg_win | 8.5883 |
| net_avg_loss | -14.4715 |
| avg_hold_time_bars | 3.2215 |
| exposure | 0.2573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
