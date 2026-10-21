# EMA Hourly Continuation — SUN/USDT P100_144

**Symbol:** SUN/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.3450 |
| net_win_rate | 0.3893 |
| gross_profit_factor | 0.7174 |
| gross_win_rate | 0.4036 |
| sharpe_ratio | -5.6643 |
| sortino_ratio | -1.3841 |
| max_drawdown | 0.8131 |
| cagr | -0.4839 |
| net_avg_win | 39.2154 |
| net_avg_loss | -72.4519 |
| avg_hold_time_bars | 8.9107 |
| exposure | 0.1129 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
