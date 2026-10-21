# EMA Hourly Continuation — BRETT/USDT P100_200

**Symbol:** BRETT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 0.8053 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 0.9558 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -1.0932 |
| sortino_ratio | -0.2493 |
| max_drawdown | 0.3148 |
| cagr | -0.1095 |
| net_avg_win | 84.2938 |
| net_avg_loss | -100.4142 |
| avg_hold_time_bars | 13.6929 |
| exposure | 0.1588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
