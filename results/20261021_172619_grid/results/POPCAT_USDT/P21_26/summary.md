# EMA Hourly Continuation — POPCAT/USDT P21_26

**Symbol:** POPCAT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 191 |
| net_profit_factor | 0.5006 |
| net_win_rate | 0.3979 |
| gross_profit_factor | 0.6665 |
| gross_win_rate | 0.3979 |
| sharpe_ratio | -3.2772 |
| sortino_ratio | -0.6922 |
| max_drawdown | 0.5077 |
| cagr | -0.2746 |
| net_avg_win | 65.9988 |
| net_avg_loss | -87.1252 |
| avg_hold_time_bars | 4.5445 |
| exposure | 0.0459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
