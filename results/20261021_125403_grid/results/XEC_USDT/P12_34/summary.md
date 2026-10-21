# EMA Hourly Continuation — XEC/USDT P12_34

**Symbol:** XEC/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 756 |
| net_profit_factor | 0.6536 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9671 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -3.8897 |
| sortino_ratio | -1.5318 |
| max_drawdown | 0.8397 |
| cagr | -0.5017 |
| net_avg_win | 42.4319 |
| net_avg_loss | -61.5706 |
| avg_hold_time_bars | 6.7050 |
| exposure | 0.2294 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
