# EMA Hourly Continuation — XPR/USDT P12_89

**Symbol:** XPR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.7082 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.8785 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -2.6347 |
| sortino_ratio | -0.8452 |
| max_drawdown | 0.6631 |
| cagr | -0.3220 |
| net_avg_win | 63.8206 |
| net_avg_loss | -78.2319 |
| avg_hold_time_bars | 16.5471 |
| exposure | 0.3836 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
