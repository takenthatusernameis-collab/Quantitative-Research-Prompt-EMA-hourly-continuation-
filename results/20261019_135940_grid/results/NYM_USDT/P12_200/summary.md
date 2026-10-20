# EMA Hourly Continuation — NYM/USDT P12_200

**Symbol:** NYM/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.3049 |
| net_win_rate | 0.3229 |
| gross_profit_factor | 0.5313 |
| gross_win_rate | 0.3341 |
| sharpe_ratio | -7.8466 |
| sortino_ratio | -2.3388 |
| max_drawdown | 0.9541 |
| cagr | -0.7034 |
| net_avg_win | 28.8150 |
| net_avg_loss | -45.0843 |
| avg_hold_time_bars | 34.7639 |
| exposure | 0.7095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
