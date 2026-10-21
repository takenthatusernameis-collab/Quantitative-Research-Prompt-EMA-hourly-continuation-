# EMA Hourly Continuation — BTT/USDT P8_50

**Symbol:** BTT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.5904 |
| net_win_rate | 0.4732 |
| gross_profit_factor | 0.9067 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -4.4664 |
| sortino_ratio | -1.5601 |
| max_drawdown | 0.8407 |
| cagr | -0.5165 |
| net_avg_win | 42.8763 |
| net_avg_loss | -65.2191 |
| avg_hold_time_bars | 18.9631 |
| exposure | 0.5137 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
