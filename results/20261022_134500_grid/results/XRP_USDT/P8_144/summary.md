# EMA Hourly Continuation — XRP/USDT P8_144

**Symbol:** XRP/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.5400 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.9883 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -4.7000 |
| sortino_ratio | -1.4933 |
| max_drawdown | 0.8643 |
| cagr | -0.5332 |
| net_avg_win | 40.8364 |
| net_avg_loss | -65.9398 |
| avg_hold_time_bars | 30.2890 |
| exposure | 0.7242 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
