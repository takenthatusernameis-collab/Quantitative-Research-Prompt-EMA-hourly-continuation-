# EMA Hourly Continuation — PYTH/USDT P8_100

**Symbol:** PYTH/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.6522 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9028 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -3.1842 |
| sortino_ratio | -1.1067 |
| max_drawdown | 0.7608 |
| cagr | -0.4112 |
| net_avg_win | 47.0699 |
| net_avg_loss | -66.5013 |
| avg_hold_time_bars | 24.9296 |
| exposure | 0.6924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
