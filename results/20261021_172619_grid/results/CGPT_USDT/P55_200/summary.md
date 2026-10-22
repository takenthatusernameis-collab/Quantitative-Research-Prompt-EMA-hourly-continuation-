# EMA Hourly Continuation — CGPT/USDT P55_200

**Symbol:** CGPT/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.7666 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.9136 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -1.4827 |
| sortino_ratio | -0.3594 |
| max_drawdown | 0.3672 |
| cagr | -0.1533 |
| net_avg_win | 81.3013 |
| net_avg_loss | -96.2874 |
| avg_hold_time_bars | 26.8517 |
| exposure | 0.3540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
