# EMA Hourly Continuation — CARV/USDT P12_21

**Symbol:** CARV/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1067 |
| net_profit_factor | 0.4168 |
| net_win_rate | 0.4339 |
| gross_profit_factor | 0.8979 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -10.9931 |
| sortino_ratio | -5.6736 |
| max_drawdown | 0.9970 |
| cagr | -0.9422 |
| net_avg_win | 15.3865 |
| net_avg_loss | -28.2999 |
| avg_hold_time_bars | 3.2830 |
| exposure | 0.1971 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
