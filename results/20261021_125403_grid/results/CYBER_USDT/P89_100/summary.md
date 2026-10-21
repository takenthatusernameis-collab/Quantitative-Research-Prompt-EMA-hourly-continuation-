# EMA Hourly Continuation — CYBER/USDT P89_100

**Symbol:** CYBER/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 174 |
| net_profit_factor | 0.5757 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.8804 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -2.1031 |
| sortino_ratio | -0.3981 |
| max_drawdown | 0.3785 |
| cagr | -0.1667 |
| net_avg_win | 60.0707 |
| net_avg_loss | -95.1772 |
| avg_hold_time_bars | 5.2874 |
| exposure | 0.0418 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
