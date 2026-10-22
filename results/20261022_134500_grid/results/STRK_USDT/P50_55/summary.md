# EMA Hourly Continuation — STRK/USDT P50_55

**Symbol:** STRK/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 814 |
| net_profit_factor | 0.2505 |
| net_win_rate | 0.3636 |
| gross_profit_factor | 0.6939 |
| gross_win_rate | 0.4091 |
| sharpe_ratio | -11.7197 |
| sortino_ratio | -4.8975 |
| max_drawdown | 0.9986 |
| cagr | -0.9269 |
| net_avg_win | 11.2734 |
| net_avg_loss | -25.7199 |
| avg_hold_time_bars | 1.7899 |
| exposure | 0.0662 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
