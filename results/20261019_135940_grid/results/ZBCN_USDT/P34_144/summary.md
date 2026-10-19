# EMA Hourly Continuation — ZBCN/USDT P34_144

**Symbol:** ZBCN/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.6553 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9131 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -3.3260 |
| sortino_ratio | -1.1621 |
| max_drawdown | 0.7675 |
| cagr | -0.4281 |
| net_avg_win | 48.6926 |
| net_avg_loss | -67.8080 |
| avg_hold_time_bars | 11.9085 |
| exposure | 0.3372 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
