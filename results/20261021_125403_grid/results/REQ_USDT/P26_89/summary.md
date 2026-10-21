# EMA Hourly Continuation — REQ/USDT P26_89

**Symbol:** REQ/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.6348 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.9226 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -3.6881 |
| sortino_ratio | -1.1999 |
| max_drawdown | 0.7572 |
| cagr | -0.4246 |
| net_avg_win | 53.9004 |
| net_avg_loss | -74.1798 |
| avg_hold_time_bars | 12.9961 |
| exposure | 0.3066 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
