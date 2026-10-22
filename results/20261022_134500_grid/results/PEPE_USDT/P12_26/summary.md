# EMA Hourly Continuation — PEPE/USDT P12_26

**Symbol:** PEPE/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1395 |
| net_profit_factor | 0.4592 |
| net_win_rate | 0.4108 |
| gross_profit_factor | 0.8277 |
| gross_win_rate | 0.4308 |
| sharpe_ratio | -11.3671 |
| sortino_ratio | -6.0026 |
| max_drawdown | 0.9995 |
| cagr | -0.9520 |
| net_avg_win | 14.8096 |
| net_avg_loss | -22.4830 |
| avg_hold_time_bars | 2.6487 |
| exposure | 0.1680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
