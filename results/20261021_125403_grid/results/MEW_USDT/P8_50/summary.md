# EMA Hourly Continuation — MEW/USDT P8_50

**Symbol:** MEW/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 694 |
| net_profit_factor | 0.7475 |
| net_win_rate | 0.4798 |
| gross_profit_factor | 0.9145 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -2.5169 |
| sortino_ratio | -0.9449 |
| max_drawdown | 0.6772 |
| cagr | -0.3523 |
| net_avg_win | 59.0373 |
| net_avg_loss | -72.8530 |
| avg_hold_time_bars | 13.1916 |
| exposure | 0.4161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
