# EMA Hourly Continuation — ATOM/USDT P12_26

**Symbol:** ATOM/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1380 |
| net_profit_factor | 0.2708 |
| net_win_rate | 0.4130 |
| gross_profit_factor | 0.7097 |
| gross_win_rate | 0.4442 |
| sharpe_ratio | -12.1500 |
| sortino_ratio | -6.4451 |
| max_drawdown | 0.9997 |
| cagr | -0.9612 |
| net_avg_win | 6.5126 |
| net_avg_loss | -16.9251 |
| avg_hold_time_bars | 2.8036 |
| exposure | 0.1759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
