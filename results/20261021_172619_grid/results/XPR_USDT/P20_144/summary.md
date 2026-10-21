# EMA Hourly Continuation — XPR/USDT P20_144

**Symbol:** XPR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.6563 |
| net_win_rate | 0.4580 |
| gross_profit_factor | 0.8079 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -2.2259 |
| sortino_ratio | -0.5862 |
| max_drawdown | 0.5100 |
| cagr | -0.2366 |
| net_avg_win | 59.5011 |
| net_avg_loss | -76.6042 |
| avg_hold_time_bars | 29.3797 |
| exposure | 0.4607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
