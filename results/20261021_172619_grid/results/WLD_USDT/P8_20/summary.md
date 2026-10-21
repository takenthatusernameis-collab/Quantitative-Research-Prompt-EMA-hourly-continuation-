# EMA Hourly Continuation — WLD/USDT P8_20

**Symbol:** WLD/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.9497 |
| net_win_rate | 0.5538 |
| gross_profit_factor | 1.2220 |
| gross_win_rate | 0.5538 |
| sharpe_ratio | -0.2603 |
| sortino_ratio | -0.0799 |
| max_drawdown | 0.2034 |
| cagr | -0.0424 |
| net_avg_win | 78.8350 |
| net_avg_loss | -103.0346 |
| avg_hold_time_bars | 5.3408 |
| exposure | 0.1083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
