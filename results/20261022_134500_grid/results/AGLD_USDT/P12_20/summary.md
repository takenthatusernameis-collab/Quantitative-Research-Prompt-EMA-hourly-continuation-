# EMA Hourly Continuation — AGLD/USDT P12_20

**Symbol:** AGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1373 |
| net_profit_factor | 0.3293 |
| net_win_rate | 0.4086 |
| gross_profit_factor | 0.8250 |
| gross_win_rate | 0.4465 |
| sharpe_ratio | -11.5136 |
| sortino_ratio | -6.0661 |
| max_drawdown | 0.9995 |
| cagr | -0.9507 |
| net_avg_win | 8.7466 |
| net_avg_loss | -18.3519 |
| avg_hold_time_bars | 3.1529 |
| exposure | 0.1959 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
