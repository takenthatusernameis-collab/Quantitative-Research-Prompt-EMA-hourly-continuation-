# EMA Hourly Continuation — COMP/USDT P50_89

**Symbol:** COMP/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 714 |
| net_profit_factor | 0.4307 |
| net_win_rate | 0.4678 |
| gross_profit_factor | 0.8672 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -5.8785 |
| sortino_ratio | -2.2053 |
| max_drawdown | 0.9359 |
| cagr | -0.6622 |
| net_avg_win | 21.1705 |
| net_avg_loss | -43.2000 |
| avg_hold_time_bars | 4.9734 |
| exposure | 0.1614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
