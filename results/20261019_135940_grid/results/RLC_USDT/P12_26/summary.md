# EMA Hourly Continuation — RLC/USDT P12_26

**Symbol:** RLC/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1288 |
| net_profit_factor | 0.4742 |
| net_win_rate | 0.4511 |
| gross_profit_factor | 0.9780 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -9.2283 |
| sortino_ratio | -4.6839 |
| max_drawdown | 0.9971 |
| cagr | -0.9003 |
| net_avg_win | 15.4770 |
| net_avg_loss | -26.8197 |
| avg_hold_time_bars | 3.5761 |
| exposure | 0.2094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
