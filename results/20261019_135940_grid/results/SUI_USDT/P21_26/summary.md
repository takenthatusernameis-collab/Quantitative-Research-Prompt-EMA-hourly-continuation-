# EMA Hourly Continuation — SUI/USDT P21_26

**Symbol:** SUI/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1215 |
| net_profit_factor | 0.2890 |
| net_win_rate | 0.3597 |
| gross_profit_factor | 0.7497 |
| gross_win_rate | 0.3984 |
| sharpe_ratio | -14.7070 |
| sortino_ratio | -7.4309 |
| max_drawdown | 1.0000 |
| cagr | -0.9824 |
| net_avg_win | 9.3023 |
| net_avg_loss | -18.0780 |
| avg_hold_time_bars | 1.7942 |
| exposure | 0.0991 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
