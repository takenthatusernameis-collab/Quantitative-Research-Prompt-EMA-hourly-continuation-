# EMA Hourly Continuation — SNX/USDT P20_55

**Symbol:** SNX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.7999 |
| net_win_rate | 0.5122 |
| gross_profit_factor | 1.0487 |
| gross_win_rate | 0.5122 |
| sharpe_ratio | -1.6412 |
| sortino_ratio | -0.5437 |
| max_drawdown | 0.5197 |
| cagr | -0.2214 |
| net_avg_win | 68.5145 |
| net_avg_loss | -89.9412 |
| avg_hold_time_bars | 8.2008 |
| exposure | 0.1978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
