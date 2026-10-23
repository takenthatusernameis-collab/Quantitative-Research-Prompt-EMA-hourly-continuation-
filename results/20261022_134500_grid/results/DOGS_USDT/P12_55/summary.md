# EMA Hourly Continuation — DOGS/USDT P12_55

**Symbol:** DOGS/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 871 |
| net_profit_factor | 0.5790 |
| net_win_rate | 0.4592 |
| gross_profit_factor | 0.8682 |
| gross_win_rate | 0.4638 |
| sharpe_ratio | -6.0590 |
| sortino_ratio | -2.6877 |
| max_drawdown | 0.9429 |
| cagr | -0.7345 |
| net_avg_win | 32.3981 |
| net_avg_loss | -47.5214 |
| avg_hold_time_bars | 8.5913 |
| exposure | 0.3970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
