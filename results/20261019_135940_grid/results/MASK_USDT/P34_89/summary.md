# EMA Hourly Continuation — MASK/USDT P34_89

**Symbol:** MASK/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 742 |
| net_profit_factor | 0.4073 |
| net_win_rate | 0.4407 |
| gross_profit_factor | 0.7643 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -6.4900 |
| sortino_ratio | -2.5056 |
| max_drawdown | 0.9547 |
| cagr | -0.7029 |
| net_avg_win | 20.0142 |
| net_avg_loss | -38.7232 |
| avg_hold_time_bars | 7.1658 |
| exposure | 0.2417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
