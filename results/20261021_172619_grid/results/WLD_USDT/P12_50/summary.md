# EMA Hourly Continuation — WLD/USDT P12_50

**Symbol:** WLD/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 588 |
| net_profit_factor | 0.8253 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 0.9998 |
| gross_win_rate | 0.4966 |
| sharpe_ratio | -1.5776 |
| sortino_ratio | -0.5475 |
| max_drawdown | 0.5429 |
| cagr | -0.2242 |
| net_avg_win | 76.2568 |
| net_avg_loss | -91.1527 |
| avg_hold_time_bars | 11.6054 |
| exposure | 0.3102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
