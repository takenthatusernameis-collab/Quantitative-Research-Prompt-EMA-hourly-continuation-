# EMA Hourly Continuation — LUNA/USDT P12_50

**Symbol:** LUNA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.6672 |
| net_win_rate | 0.4430 |
| gross_profit_factor | 0.8629 |
| gross_win_rate | 0.4430 |
| sharpe_ratio | -3.7936 |
| sortino_ratio | -1.3155 |
| max_drawdown | 0.7865 |
| cagr | -0.4544 |
| net_avg_win | 59.3646 |
| net_avg_loss | -70.7490 |
| avg_hold_time_bars | 9.7987 |
| exposure | 0.2655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
