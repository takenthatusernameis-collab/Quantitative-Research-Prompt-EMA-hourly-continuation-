# EMA Hourly Continuation — REQ/USDT P8_12

**Symbol:** REQ/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1852 |
| net_profit_factor | 0.1490 |
| net_win_rate | 0.2802 |
| gross_profit_factor | 0.5340 |
| gross_win_rate | 0.3688 |
| sharpe_ratio | -22.5354 |
| sortino_ratio | -14.5955 |
| max_drawdown | 1.0000 |
| cagr | -0.9997 |
| net_avg_win | 3.3723 |
| net_avg_loss | -8.8149 |
| avg_hold_time_bars | 2.2111 |
| exposure | 0.1861 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
