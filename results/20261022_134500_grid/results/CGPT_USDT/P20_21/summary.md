# EMA Hourly Continuation — CGPT/USDT P20_21

**Symbol:** CGPT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1156 |
| net_profit_factor | 0.1250 |
| net_win_rate | 0.2777 |
| gross_profit_factor | 0.6046 |
| gross_win_rate | 0.3529 |
| sharpe_ratio | -17.8362 |
| sortino_ratio | -9.2544 |
| max_drawdown | 1.0000 |
| cagr | -0.9946 |
| net_avg_win | 4.4523 |
| net_avg_loss | -13.6876 |
| avg_hold_time_bars | 1.7050 |
| exposure | 0.0896 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
