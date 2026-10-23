# EMA Hourly Continuation — TRB/USDT P20_89

**Symbol:** TRB/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 681 |
| net_profit_factor | 0.4608 |
| net_win_rate | 0.4170 |
| gross_profit_factor | 0.7684 |
| gross_win_rate | 0.4420 |
| sharpe_ratio | -6.1717 |
| sortino_ratio | -2.2538 |
| max_drawdown | 0.9391 |
| cagr | -0.6663 |
| net_avg_win | 28.2060 |
| net_avg_loss | -43.7854 |
| avg_hold_time_bars | 14.4728 |
| exposure | 0.4460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
