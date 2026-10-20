# EMA Hourly Continuation — CSPR/USDT P21_100

**Symbol:** CSPR/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 951 |
| net_profit_factor | 0.4825 |
| net_win_rate | 0.4154 |
| gross_profit_factor | 0.8115 |
| gross_win_rate | 0.4259 |
| sharpe_ratio | -7.2622 |
| sortino_ratio | -3.1453 |
| max_drawdown | 0.9795 |
| cagr | -0.7830 |
| net_avg_win | 23.0917 |
| net_avg_loss | -34.0027 |
| avg_hold_time_bars | 8.8843 |
| exposure | 0.3840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
