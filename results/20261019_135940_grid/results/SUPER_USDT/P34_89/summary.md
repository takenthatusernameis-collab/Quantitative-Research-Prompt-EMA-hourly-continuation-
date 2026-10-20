# EMA Hourly Continuation — SUPER/USDT P34_89

**Symbol:** SUPER/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.6389 |
| net_win_rate | 0.5031 |
| gross_profit_factor | 0.9778 |
| gross_win_rate | 0.5123 |
| sharpe_ratio | -3.1599 |
| sortino_ratio | -1.1396 |
| max_drawdown | 0.7607 |
| cagr | -0.4153 |
| net_avg_win | 40.1743 |
| net_avg_loss | -63.6602 |
| avg_hold_time_bars | 9.4043 |
| exposure | 0.2770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
