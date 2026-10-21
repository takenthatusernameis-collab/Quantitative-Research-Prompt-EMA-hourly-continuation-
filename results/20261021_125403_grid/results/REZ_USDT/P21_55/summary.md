# EMA Hourly Continuation — REZ/USDT P21_55

**Symbol:** REZ/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.8234 |
| net_win_rate | 0.5037 |
| gross_profit_factor | 1.0357 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -1.6631 |
| sortino_ratio | -0.5592 |
| max_drawdown | 0.5989 |
| cagr | -0.2277 |
| net_avg_win | 80.6717 |
| net_avg_loss | -99.4332 |
| avg_hold_time_bars | 8.6236 |
| exposure | 0.2156 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
