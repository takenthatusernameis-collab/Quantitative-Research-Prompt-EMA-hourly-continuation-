# EMA Hourly Continuation — CFG/USDT P26_50

**Symbol:** CFG/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 300 |
| net_profit_factor | 0.5753 |
| net_win_rate | 0.4400 |
| gross_profit_factor | 0.7570 |
| gross_win_rate | 0.4400 |
| sharpe_ratio | -2.7334 |
| sortino_ratio | -0.6719 |
| max_drawdown | 0.5601 |
| cagr | -0.2663 |
| net_avg_win | 55.4642 |
| net_avg_loss | -75.7507 |
| avg_hold_time_bars | 24.9833 |
| exposure | 0.3407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
