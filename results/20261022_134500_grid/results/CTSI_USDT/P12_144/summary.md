# EMA Hourly Continuation — CTSI/USDT P12_144

**Symbol:** CTSI/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.6978 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 1.0072 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -2.8108 |
| sortino_ratio | -0.8857 |
| max_drawdown | 0.6665 |
| cagr | -0.3375 |
| net_avg_win | 63.8643 |
| net_avg_loss | -82.0149 |
| avg_hold_time_bars | 29.8337 |
| exposure | 0.6685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
