# EMA Hourly Continuation — GRAM/USDT P21_55

**Symbol:** GRAM/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.6062 |
| net_win_rate | 0.4602 |
| gross_profit_factor | 0.8713 |
| gross_win_rate | 0.4602 |
| sharpe_ratio | -3.4272 |
| sortino_ratio | -1.0412 |
| max_drawdown | 0.7017 |
| cagr | -0.3795 |
| net_avg_win | 51.6836 |
| net_avg_loss | -72.6786 |
| avg_hold_time_bars | 8.1792 |
| exposure | 0.1680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
