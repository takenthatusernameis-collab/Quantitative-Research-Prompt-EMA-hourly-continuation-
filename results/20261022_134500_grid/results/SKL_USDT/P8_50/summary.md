# EMA Hourly Continuation — SKL/USDT P8_50

**Symbol:** SKL/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1154 |
| net_profit_factor | 0.6462 |
| net_win_rate | 0.4801 |
| gross_profit_factor | 1.0124 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -5.4969 |
| sortino_ratio | -2.6191 |
| max_drawdown | 0.9594 |
| cagr | -0.7167 |
| net_avg_win | 31.5829 |
| net_avg_loss | -45.1264 |
| avg_hold_time_bars | 8.8804 |
| exposure | 0.4658 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
