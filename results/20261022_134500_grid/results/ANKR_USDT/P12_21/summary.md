# EMA Hourly Continuation — ANKR/USDT P12_21

**Symbol:** ANKR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1466 |
| net_profit_factor | 0.2885 |
| net_win_rate | 0.3840 |
| gross_profit_factor | 0.7405 |
| gross_win_rate | 0.4216 |
| sharpe_ratio | -14.4732 |
| sortino_ratio | -7.9545 |
| max_drawdown | 1.0000 |
| cagr | -0.9837 |
| net_avg_win | 7.2031 |
| net_avg_loss | -15.5648 |
| avg_hold_time_bars | 2.9072 |
| exposure | 0.1937 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
