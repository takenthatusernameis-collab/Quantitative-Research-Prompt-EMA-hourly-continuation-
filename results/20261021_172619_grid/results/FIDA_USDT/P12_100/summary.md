# EMA Hourly Continuation — FIDA/USDT P12_100

**Symbol:** FIDA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.7092 |
| net_win_rate | 0.4788 |
| gross_profit_factor | 0.8851 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -2.1712 |
| sortino_ratio | -0.6863 |
| max_drawdown | 0.5729 |
| cagr | -0.2714 |
| net_avg_win | 56.6109 |
| net_avg_loss | -73.3249 |
| avg_hold_time_bars | 26.1010 |
| exposure | 0.5846 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
