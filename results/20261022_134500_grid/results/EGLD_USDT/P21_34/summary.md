# EMA Hourly Continuation — EGLD/USDT P21_34

**Symbol:** EGLD/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1163 |
| net_profit_factor | 0.2850 |
| net_win_rate | 0.3981 |
| gross_profit_factor | 0.7740 |
| gross_win_rate | 0.4291 |
| sharpe_ratio | -11.9631 |
| sortino_ratio | -5.8259 |
| max_drawdown | 0.9995 |
| cagr | -0.9510 |
| net_avg_win | 8.6048 |
| net_avg_loss | -19.9698 |
| avg_hold_time_bars | 2.5830 |
| exposure | 0.1365 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
