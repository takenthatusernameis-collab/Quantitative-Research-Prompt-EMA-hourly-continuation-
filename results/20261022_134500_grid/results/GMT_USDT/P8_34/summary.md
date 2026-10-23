# EMA Hourly Continuation — GMT/USDT P8_34

**Symbol:** GMT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1416 |
| net_profit_factor | 0.3791 |
| net_win_rate | 0.4287 |
| gross_profit_factor | 0.7493 |
| gross_win_rate | 0.4449 |
| sharpe_ratio | -9.7516 |
| sortino_ratio | -5.1512 |
| max_drawdown | 0.9984 |
| cagr | -0.9228 |
| net_avg_win | 10.0407 |
| net_avg_loss | -19.8747 |
| avg_hold_time_bars | 5.3404 |
| exposure | 0.3437 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
