# EMA Hourly Continuation — MINA/USDT P100_200

**Symbol:** MINA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.8199 |
| net_win_rate | 0.5241 |
| gross_profit_factor | 1.0830 |
| gross_win_rate | 0.5241 |
| sharpe_ratio | -0.9986 |
| sortino_ratio | -0.2448 |
| max_drawdown | 0.2794 |
| cagr | -0.1077 |
| net_avg_win | 74.5306 |
| net_avg_loss | -100.1256 |
| avg_hold_time_bars | 13.8517 |
| exposure | 0.1826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
