# EMA Hourly Continuation — RIO/USDT P26_200

**Symbol:** RIO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.8097 |
| net_win_rate | 0.4719 |
| gross_profit_factor | 0.9002 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -1.1775 |
| sortino_ratio | -0.2924 |
| max_drawdown | 0.3673 |
| cagr | -0.1278 |
| net_avg_win | 85.7614 |
| net_avg_loss | -94.6624 |
| avg_hold_time_bars | 39.5842 |
| exposure | 0.5506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
