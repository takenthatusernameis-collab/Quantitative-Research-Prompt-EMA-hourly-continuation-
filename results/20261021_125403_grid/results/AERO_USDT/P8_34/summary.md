# EMA Hourly Continuation — AERO/USDT P8_34

**Symbol:** AERO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 720 |
| net_profit_factor | 0.8802 |
| net_win_rate | 0.5208 |
| gross_profit_factor | 1.0963 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -1.2217 |
| sortino_ratio | -0.4715 |
| max_drawdown | 0.5661 |
| cagr | -0.1985 |
| net_avg_win | 83.5024 |
| net_avg_loss | -103.1216 |
| avg_hold_time_bars | 8.5000 |
| exposure | 0.2782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
