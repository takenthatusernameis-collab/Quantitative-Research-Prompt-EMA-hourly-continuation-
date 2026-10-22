# EMA Hourly Continuation — COMP/USDT P12_55

**Symbol:** COMP/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1027 |
| net_profit_factor | 0.4795 |
| net_win_rate | 0.4596 |
| gross_profit_factor | 0.8306 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -6.8196 |
| sortino_ratio | -3.0730 |
| max_drawdown | 0.9769 |
| cagr | -0.7770 |
| net_avg_win | 19.0646 |
| net_avg_loss | -33.8155 |
| avg_hold_time_bars | 9.4752 |
| exposure | 0.4423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
