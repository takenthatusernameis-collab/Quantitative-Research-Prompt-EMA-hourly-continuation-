# EMA Hourly Continuation — AR/USDT P21_144

**Symbol:** AR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.6245 |
| net_win_rate | 0.4547 |
| gross_profit_factor | 0.8424 |
| gross_win_rate | 0.4612 |
| sharpe_ratio | -3.1759 |
| sortino_ratio | -0.9623 |
| max_drawdown | 0.6860 |
| cagr | -0.3661 |
| net_avg_win | 53.7249 |
| net_avg_loss | -71.7527 |
| avg_hold_time_bars | 26.1358 |
| exposure | 0.5512 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
