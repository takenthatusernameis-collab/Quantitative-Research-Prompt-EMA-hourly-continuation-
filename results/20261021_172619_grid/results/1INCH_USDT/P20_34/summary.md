# EMA Hourly Continuation — 1INCH/USDT P20_34

**Symbol:** 1INCH/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.5089 |
| net_win_rate | 0.4439 |
| gross_profit_factor | 0.7692 |
| gross_win_rate | 0.4439 |
| sharpe_ratio | -3.9107 |
| sortino_ratio | -1.0825 |
| max_drawdown | 0.7140 |
| cagr | -0.3925 |
| net_avg_win | 44.5746 |
| net_avg_loss | -69.8999 |
| avg_hold_time_bars | 4.7861 |
| exposure | 0.0814 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
