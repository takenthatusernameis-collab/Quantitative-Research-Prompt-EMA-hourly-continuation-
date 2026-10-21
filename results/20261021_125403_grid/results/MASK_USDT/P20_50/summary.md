# EMA Hourly Continuation — MASK/USDT P20_50

**Symbol:** MASK/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.6245 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.9231 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -3.7704 |
| sortino_ratio | -1.3286 |
| max_drawdown | 0.7913 |
| cagr | -0.4590 |
| net_avg_win | 45.2437 |
| net_avg_loss | -65.4310 |
| avg_hold_time_bars | 7.6125 |
| exposure | 0.2107 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
