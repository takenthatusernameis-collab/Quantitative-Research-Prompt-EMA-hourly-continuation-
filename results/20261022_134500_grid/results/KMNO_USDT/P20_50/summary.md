# EMA Hourly Continuation — KMNO/USDT P20_50

**Symbol:** KMNO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 844 |
| net_profit_factor | 0.5637 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.9406 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -5.7119 |
| sortino_ratio | -2.3609 |
| max_drawdown | 0.9402 |
| cagr | -0.6799 |
| net_avg_win | 30.9151 |
| net_avg_loss | -47.7863 |
| avg_hold_time_bars | 5.2322 |
| exposure | 0.2039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
