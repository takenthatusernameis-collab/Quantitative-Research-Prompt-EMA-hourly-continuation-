# EMA Hourly Continuation — VR/USDT P8_20

**Symbol:** VR/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1686 |
| net_profit_factor | 0.3592 |
| net_win_rate | 0.3078 |
| gross_profit_factor | 0.6540 |
| gross_win_rate | 0.3333 |
| sharpe_ratio | -19.3355 |
| sortino_ratio | -11.4698 |
| max_drawdown | 1.0000 |
| cagr | -0.9987 |
| net_avg_win | 10.7988 |
| net_avg_loss | -13.3715 |
| avg_hold_time_bars | 3.4342 |
| exposure | 0.2632 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
