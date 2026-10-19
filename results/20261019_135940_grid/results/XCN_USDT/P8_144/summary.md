# EMA Hourly Continuation — XCN/USDT P8_144

**Symbol:** XCN/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 767 |
| net_profit_factor | 0.5006 |
| net_win_rate | 0.4276 |
| gross_profit_factor | 0.7738 |
| gross_win_rate | 0.4394 |
| sharpe_ratio | -6.1400 |
| sortino_ratio | -2.3767 |
| max_drawdown | 0.9478 |
| cagr | -0.6899 |
| net_avg_win | 28.9469 |
| net_avg_loss | -43.2032 |
| avg_hold_time_bars | 19.3286 |
| exposure | 0.6739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
