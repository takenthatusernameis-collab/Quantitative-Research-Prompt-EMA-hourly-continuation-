# EMA Hourly Continuation — EDU/USDT P20_26

**Symbol:** EDU/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1241 |
| net_profit_factor | 0.2737 |
| net_win_rate | 0.3795 |
| gross_profit_factor | 0.6755 |
| gross_win_rate | 0.4166 |
| sharpe_ratio | -12.4263 |
| sortino_ratio | -6.2673 |
| max_drawdown | 0.9996 |
| cagr | -0.9569 |
| net_avg_win | 7.9986 |
| net_avg_loss | -17.8750 |
| avg_hold_time_bars | 2.4142 |
| exposure | 0.1356 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
