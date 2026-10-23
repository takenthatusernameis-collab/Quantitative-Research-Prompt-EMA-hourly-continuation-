# EMA Hourly Continuation — WAVES/USDT P12_200

**Symbol:** WAVES/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 580 |
| net_profit_factor | 0.5301 |
| net_win_rate | 0.4552 |
| gross_profit_factor | 0.8849 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -4.7558 |
| sortino_ratio | -1.5920 |
| max_drawdown | 0.8724 |
| cagr | -0.5497 |
| net_avg_win | 36.9692 |
| net_avg_loss | -58.2630 |
| avg_hold_time_bars | 25.8190 |
| exposure | 0.6807 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
