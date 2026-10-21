# EMA Hourly Continuation — STRAX/USDT P21_89

**Symbol:** STRAX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.6288 |
| net_win_rate | 0.4455 |
| gross_profit_factor | 0.8427 |
| gross_win_rate | 0.4473 |
| sharpe_ratio | -3.8709 |
| sortino_ratio | -1.2918 |
| max_drawdown | 0.7879 |
| cagr | -0.4497 |
| net_avg_win | 53.5706 |
| net_avg_loss | -68.4387 |
| avg_hold_time_bars | 14.1855 |
| exposure | 0.3567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
