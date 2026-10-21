# EMA Hourly Continuation — MNT/USDT P21_34

**Symbol:** MNT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.5872 |
| net_win_rate | 0.4804 |
| gross_profit_factor | 0.9590 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -3.4509 |
| sortino_ratio | -0.9373 |
| max_drawdown | 0.6768 |
| cagr | -0.3503 |
| net_avg_win | 54.6878 |
| net_avg_loss | -86.1294 |
| avg_hold_time_bars | 5.7011 |
| exposure | 0.0928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
