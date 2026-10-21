# EMA Hourly Continuation — XDC/USDT P20_34

**Symbol:** XDC/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.5266 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.8705 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -3.0213 |
| sortino_ratio | -0.7386 |
| max_drawdown | 0.5760 |
| cagr | -0.2855 |
| net_avg_win | 45.9436 |
| net_avg_loss | -80.2714 |
| avg_hold_time_bars | 6.8924 |
| exposure | 0.0902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
