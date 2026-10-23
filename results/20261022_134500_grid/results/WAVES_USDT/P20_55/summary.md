# EMA Hourly Continuation — WAVES/USDT P20_55

**Symbol:** WAVES/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1114 |
| net_profit_factor | 0.4201 |
| net_win_rate | 0.3932 |
| gross_profit_factor | 0.8759 |
| gross_win_rate | 0.4237 |
| sharpe_ratio | -10.7519 |
| sortino_ratio | -5.0782 |
| max_drawdown | 0.9984 |
| cagr | -0.9233 |
| net_avg_win | 16.5102 |
| net_avg_loss | -25.4669 |
| avg_hold_time_bars | 5.0458 |
| exposure | 0.2555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
