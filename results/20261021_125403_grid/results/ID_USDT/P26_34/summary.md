# EMA Hourly Continuation — ID/USDT P26_34

**Symbol:** ID/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.6307 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0060 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.7085 |
| sortino_ratio | -0.7304 |
| max_drawdown | 0.5854 |
| cagr | -0.2835 |
| net_avg_win | 55.1749 |
| net_avg_loss | -87.4869 |
| avg_hold_time_bars | 5.0994 |
| exposure | 0.0812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
