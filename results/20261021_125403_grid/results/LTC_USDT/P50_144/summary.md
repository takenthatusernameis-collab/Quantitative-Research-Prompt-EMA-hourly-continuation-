# EMA Hourly Continuation — LTC/USDT P50_144

**Symbol:** LTC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.5469 |
| net_win_rate | 0.4478 |
| gross_profit_factor | 0.7788 |
| gross_win_rate | 0.4478 |
| sharpe_ratio | -3.1714 |
| sortino_ratio | -0.8273 |
| max_drawdown | 0.6323 |
| cagr | -0.3168 |
| net_avg_win | 49.5536 |
| net_avg_loss | -73.4698 |
| avg_hold_time_bars | 17.2567 |
| exposure | 0.2628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
