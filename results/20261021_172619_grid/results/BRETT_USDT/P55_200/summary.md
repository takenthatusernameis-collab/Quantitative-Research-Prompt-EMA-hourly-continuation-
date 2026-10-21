# EMA Hourly Continuation — BRETT/USDT P55_200

**Symbol:** BRETT/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 0.6886 |
| net_win_rate | 0.4389 |
| gross_profit_factor | 0.7836 |
| gross_win_rate | 0.4389 |
| sharpe_ratio | -1.9507 |
| sortino_ratio | -0.4586 |
| max_drawdown | 0.4063 |
| cagr | -0.1907 |
| net_avg_win | 75.8639 |
| net_avg_loss | -86.1931 |
| avg_hold_time_bars | 32.0916 |
| exposure | 0.4046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
