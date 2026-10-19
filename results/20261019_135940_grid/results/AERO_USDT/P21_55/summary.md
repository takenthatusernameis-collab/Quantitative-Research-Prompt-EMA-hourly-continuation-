# EMA Hourly Continuation — AERO/USDT P21_55

**Symbol:** AERO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 864 |
| net_profit_factor | 0.5132 |
| net_win_rate | 0.4664 |
| gross_profit_factor | 0.8364 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -5.5428 |
| sortino_ratio | -2.2798 |
| max_drawdown | 0.9409 |
| cagr | -0.6735 |
| net_avg_win | 24.5872 |
| net_avg_loss | -41.8812 |
| avg_hold_time_bars | 5.3090 |
| exposure | 0.2085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
