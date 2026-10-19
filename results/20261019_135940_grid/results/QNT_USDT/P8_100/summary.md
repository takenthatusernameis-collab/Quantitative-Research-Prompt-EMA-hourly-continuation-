# EMA Hourly Continuation — QNT/USDT P8_100

**Symbol:** QNT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 867 |
| net_profit_factor | 0.5684 |
| net_win_rate | 0.4740 |
| gross_profit_factor | 0.9107 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -5.0552 |
| sortino_ratio | -2.0917 |
| max_drawdown | 0.9243 |
| cagr | -0.6357 |
| net_avg_win | 29.5056 |
| net_avg_loss | -46.7865 |
| avg_hold_time_bars | 15.1649 |
| exposure | 0.5976 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
