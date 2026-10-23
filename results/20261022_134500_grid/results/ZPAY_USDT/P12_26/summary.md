# EMA Hourly Continuation — ZPAY/USDT P12_26

**Symbol:** ZPAY/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1022 |
| net_profit_factor | 0.4008 |
| net_win_rate | 0.3415 |
| gross_profit_factor | 0.6888 |
| gross_win_rate | 0.3523 |
| sharpe_ratio | -9.8804 |
| sortino_ratio | -4.4153 |
| max_drawdown | 0.9951 |
| cagr | -0.8782 |
| net_avg_win | 19.0746 |
| net_avg_loss | -24.6771 |
| avg_hold_time_bars | 5.7593 |
| exposure | 0.2663 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
