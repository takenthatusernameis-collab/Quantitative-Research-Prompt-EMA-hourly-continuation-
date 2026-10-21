# EMA Hourly Continuation — AERO/USDT P26_200

**Symbol:** AERO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 0.9980 |
| net_win_rate | 0.5375 |
| gross_profit_factor | 1.1529 |
| gross_win_rate | 0.5375 |
| sharpe_ratio | 0.0393 |
| sortino_ratio | 0.0090 |
| max_drawdown | 0.2071 |
| cagr | -0.0011 |
| net_avg_win | 101.3504 |
| net_avg_loss | -118.0407 |
| avg_hold_time_bars | 51.2253 |
| exposure | 0.5891 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
