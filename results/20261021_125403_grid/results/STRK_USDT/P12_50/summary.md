# EMA Hourly Continuation — STRK/USDT P12_50

**Symbol:** STRK/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 576 |
| net_profit_factor | 0.7648 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 0.9510 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -1.9907 |
| sortino_ratio | -0.6829 |
| max_drawdown | 0.5570 |
| cagr | -0.2700 |
| net_avg_win | 62.9962 |
| net_avg_loss | -79.0046 |
| avg_hold_time_bars | 11.9757 |
| exposure | 0.3135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
