# EMA Hourly Continuation — UQC/USDT P12_26

**Symbol:** UQC/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.1152 |
| net_win_rate | 0.2402 |
| gross_profit_factor | 0.3552 |
| gross_win_rate | 0.2814 |
| sharpe_ratio | -11.6129 |
| sortino_ratio | -3.9324 |
| max_drawdown | 0.9960 |
| cagr | -0.8884 |
| net_avg_win | 10.1273 |
| net_avg_loss | -27.7942 |
| avg_hold_time_bars | 22.8649 |
| exposure | 0.5516 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
