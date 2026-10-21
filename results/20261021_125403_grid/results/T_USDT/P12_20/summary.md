# EMA Hourly Continuation — T/USDT P12_20

**Symbol:** T/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.5905 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.9963 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -4.4464 |
| sortino_ratio | -1.4832 |
| max_drawdown | 0.8274 |
| cagr | -0.4973 |
| net_avg_win | 46.2075 |
| net_avg_loss | -70.8129 |
| avg_hold_time_bars | 5.8928 |
| exposure | 0.1443 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
