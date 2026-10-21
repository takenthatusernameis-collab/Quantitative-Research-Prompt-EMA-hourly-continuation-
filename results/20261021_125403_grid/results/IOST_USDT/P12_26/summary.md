# EMA Hourly Continuation — IOST/USDT P12_26

**Symbol:** IOST/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.6075 |
| net_win_rate | 0.4720 |
| gross_profit_factor | 0.9467 |
| gross_win_rate | 0.4735 |
| sharpe_ratio | -4.5148 |
| sortino_ratio | -1.6674 |
| max_drawdown | 0.8569 |
| cagr | -0.5354 |
| net_avg_win | 42.3754 |
| net_avg_loss | -62.3575 |
| avg_hold_time_bars | 5.7731 |
| exposure | 0.1735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
