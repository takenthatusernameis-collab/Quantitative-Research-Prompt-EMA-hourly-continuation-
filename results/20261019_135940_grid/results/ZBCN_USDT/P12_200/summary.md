# EMA Hourly Continuation — ZBCN/USDT P12_200

**Symbol:** ZBCN/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.8712 |
| net_win_rate | 0.5272 |
| gross_profit_factor | 1.1152 |
| gross_win_rate | 0.5290 |
| sharpe_ratio | -1.0328 |
| sortino_ratio | -0.3496 |
| max_drawdown | 0.3870 |
| cagr | -0.1555 |
| net_avg_win | 79.2123 |
| net_avg_loss | -101.3790 |
| avg_hold_time_bars | 26.4783 |
| exposure | 0.6762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
