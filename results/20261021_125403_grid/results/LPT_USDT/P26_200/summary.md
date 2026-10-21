# EMA Hourly Continuation — LPT/USDT P26_200

**Symbol:** LPT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.7646 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9172 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -1.5388 |
| sortino_ratio | -0.4121 |
| max_drawdown | 0.4359 |
| cagr | -0.1734 |
| net_avg_win | 72.1964 |
| net_avg_loss | -88.2293 |
| avg_hold_time_bars | 32.1271 |
| exposure | 0.5170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
