# EMA Hourly Continuation — IOST/USDT P12_50

**Symbol:** IOST/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1014 |
| net_profit_factor | 0.5006 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.9336 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -6.8665 |
| sortino_ratio | -3.0653 |
| max_drawdown | 0.9783 |
| cagr | -0.7789 |
| net_avg_win | 21.0692 |
| net_avg_loss | -35.6488 |
| avg_hold_time_bars | 8.0237 |
| exposure | 0.3698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
