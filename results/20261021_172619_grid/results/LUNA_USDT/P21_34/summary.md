# EMA Hourly Continuation — LUNA/USDT P21_34

**Symbol:** LUNA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 247 |
| net_profit_factor | 0.5963 |
| net_win_rate | 0.4453 |
| gross_profit_factor | 0.8312 |
| gross_win_rate | 0.4453 |
| sharpe_ratio | -2.6949 |
| sortino_ratio | -0.6043 |
| max_drawdown | 0.5065 |
| cagr | -0.2425 |
| net_avg_win | 67.4382 |
| net_avg_loss | -90.8019 |
| avg_hold_time_bars | 5.5263 |
| exposure | 0.0620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
