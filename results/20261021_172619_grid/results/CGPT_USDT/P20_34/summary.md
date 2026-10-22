# EMA Hourly Continuation — CGPT/USDT P20_34

**Symbol:** CGPT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.7515 |
| net_win_rate | 0.5029 |
| gross_profit_factor | 1.0213 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -1.7622 |
| sortino_ratio | -0.4696 |
| max_drawdown | 0.4471 |
| cagr | -0.1929 |
| net_avg_win | 72.7700 |
| net_avg_loss | -97.9632 |
| avg_hold_time_bars | 5.1628 |
| exposure | 0.0807 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
