# EMA Hourly Continuation — ZETA/USDT P21_89

**Symbol:** ZETA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.8642 |
| net_win_rate | 0.5170 |
| gross_profit_factor | 1.0810 |
| gross_win_rate | 0.5170 |
| sharpe_ratio | -1.1208 |
| sortino_ratio | -0.3599 |
| max_drawdown | 0.4788 |
| cagr | -0.1550 |
| net_avg_win | 85.0536 |
| net_avg_loss | -105.3343 |
| avg_hold_time_bars | 16.5649 |
| exposure | 0.3755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
