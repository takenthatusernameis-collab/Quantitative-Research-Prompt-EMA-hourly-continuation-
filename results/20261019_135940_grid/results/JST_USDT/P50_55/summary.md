# EMA Hourly Continuation — JST/USDT P50_55

**Symbol:** JST/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.1171 |
| net_win_rate | 0.2772 |
| gross_profit_factor | 0.9382 |
| gross_win_rate | 0.4644 |
| sharpe_ratio | -13.9430 |
| sortino_ratio | -5.8071 |
| max_drawdown | 0.9997 |
| cagr | -0.9594 |
| net_avg_win | 6.9390 |
| net_avg_loss | -22.7355 |
| avg_hold_time_bars | 2.6981 |
| exposure | 0.0841 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
