# EMA Hourly Continuation — DOT/USDT P50_55

**Symbol:** DOT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 80 |
| net_profit_factor | 0.8537 |
| net_win_rate | 0.5500 |
| gross_profit_factor | 1.2087 |
| gross_win_rate | 0.5500 |
| sharpe_ratio | -0.4058 |
| sortino_ratio | -0.0527 |
| max_drawdown | 0.0887 |
| cagr | -0.0242 |
| net_avg_win | 79.1056 |
| net_avg_loss | -113.2529 |
| avg_hold_time_bars | 4.6500 |
| exposure | 0.0169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
