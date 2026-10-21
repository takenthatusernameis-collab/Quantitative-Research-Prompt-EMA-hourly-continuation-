# EMA Hourly Continuation — ROSE/USDT P55_89

**Symbol:** ROSE/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.7221 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9570 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -1.8535 |
| sortino_ratio | -0.4814 |
| max_drawdown | 0.4530 |
| cagr | -0.1983 |
| net_avg_win | 68.7353 |
| net_avg_loss | -91.2282 |
| avg_hold_time_bars | 6.4407 |
| exposure | 0.0963 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
