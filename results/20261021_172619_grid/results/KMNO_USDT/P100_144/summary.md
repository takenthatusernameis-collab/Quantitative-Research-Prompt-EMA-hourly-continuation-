# EMA Hourly Continuation — KMNO/USDT P100_144

**Symbol:** KMNO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.7320 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 0.9950 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -1.5918 |
| sortino_ratio | -0.3591 |
| max_drawdown | 0.3490 |
| cagr | -0.1534 |
| net_avg_win | 75.5404 |
| net_avg_loss | -102.3579 |
| avg_hold_time_bars | 8.3184 |
| exposure | 0.0941 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
