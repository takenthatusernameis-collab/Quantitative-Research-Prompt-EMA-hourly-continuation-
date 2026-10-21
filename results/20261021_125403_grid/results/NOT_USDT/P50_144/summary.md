# EMA Hourly Continuation — NOT/USDT P50_144

**Symbol:** NOT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.7362 |
| net_win_rate | 0.4718 |
| gross_profit_factor | 0.8961 |
| gross_win_rate | 0.4718 |
| sharpe_ratio | -1.8537 |
| sortino_ratio | -0.4924 |
| max_drawdown | 0.4244 |
| cagr | -0.2033 |
| net_avg_win | 74.5008 |
| net_avg_loss | -90.3936 |
| avg_hold_time_bars | 16.4748 |
| exposure | 0.2608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
