# EMA Hourly Continuation — MASK/USDT P12_20

**Symbol:** MASK/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.5898 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9786 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -3.6136 |
| sortino_ratio | -1.0938 |
| max_drawdown | 0.7253 |
| cagr | -0.3983 |
| net_avg_win | 48.1996 |
| net_avg_loss | -76.0625 |
| avg_hold_time_bars | 5.9327 |
| exposure | 0.1203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
