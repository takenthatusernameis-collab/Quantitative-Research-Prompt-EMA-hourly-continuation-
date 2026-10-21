# EMA Hourly Continuation — GMX/USDT P50_144

**Symbol:** GMX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.6467 |
| net_win_rate | 0.4577 |
| gross_profit_factor | 0.8376 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -2.8440 |
| sortino_ratio | -0.8454 |
| max_drawdown | 0.6367 |
| cagr | -0.3229 |
| net_avg_win | 57.1367 |
| net_avg_loss | -74.5605 |
| avg_hold_time_bars | 13.0183 |
| exposure | 0.2586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
