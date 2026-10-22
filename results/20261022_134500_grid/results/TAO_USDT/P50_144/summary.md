# EMA Hourly Continuation — TAO/USDT P50_144

**Symbol:** TAO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.7254 |
| net_win_rate | 0.5071 |
| gross_profit_factor | 1.0449 |
| gross_win_rate | 0.5112 |
| sharpe_ratio | -2.3388 |
| sortino_ratio | -0.7347 |
| max_drawdown | 0.5927 |
| cagr | -0.2933 |
| net_avg_win | 61.7370 |
| net_avg_loss | -87.5645 |
| avg_hold_time_bars | 10.7271 |
| exposure | 0.2394 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
