# EMA Hourly Continuation — EGLD/USDT P21_89

**Symbol:** EGLD/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.8363 |
| net_win_rate | 0.5202 |
| gross_profit_factor | 1.0825 |
| gross_win_rate | 0.5202 |
| sharpe_ratio | -1.2954 |
| sortino_ratio | -0.4257 |
| max_drawdown | 0.4630 |
| cagr | -0.1795 |
| net_avg_win | 73.8041 |
| net_avg_loss | -95.6680 |
| avg_hold_time_bars | 15.9846 |
| exposure | 0.3785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
