# EMA Hourly Continuation — KNC/USDT P12_100

**Symbol:** KNC/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 570 |
| net_profit_factor | 0.6122 |
| net_win_rate | 0.4491 |
| gross_profit_factor | 0.9163 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -4.3110 |
| sortino_ratio | -1.4478 |
| max_drawdown | 0.8301 |
| cagr | -0.4983 |
| net_avg_win | 50.7598 |
| net_avg_loss | -67.5973 |
| avg_hold_time_bars | 23.9684 |
| exposure | 0.6210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
