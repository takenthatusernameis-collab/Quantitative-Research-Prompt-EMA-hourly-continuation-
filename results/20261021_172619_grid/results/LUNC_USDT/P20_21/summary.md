# EMA Hourly Continuation — LUNC/USDT P20_21

**Symbol:** LUNC/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 115 |
| net_profit_factor | 0.6507 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.9231 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -1.4695 |
| sortino_ratio | -0.2259 |
| max_drawdown | 0.2562 |
| cagr | -0.0988 |
| net_avg_win | 77.8443 |
| net_avg_loss | -109.6654 |
| avg_hold_time_bars | 4.5739 |
| exposure | 0.0239 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
