# EMA Hourly Continuation — TAIKO/USDT P12_55

**Symbol:** TAIKO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 913 |
| net_profit_factor | 0.6164 |
| net_win_rate | 0.4841 |
| gross_profit_factor | 1.0235 |
| gross_win_rate | 0.4995 |
| sharpe_ratio | -5.4321 |
| sortino_ratio | -2.3522 |
| max_drawdown | 0.9405 |
| cagr | -0.6882 |
| net_avg_win | 34.0688 |
| net_avg_loss | -51.8712 |
| avg_hold_time_bars | 8.4020 |
| exposure | 0.3685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
