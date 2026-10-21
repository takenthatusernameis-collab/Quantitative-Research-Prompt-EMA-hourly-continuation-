# EMA Hourly Continuation — POL/USDT P8_20

**Symbol:** POL/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.6424 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 0.9228 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -2.6917 |
| sortino_ratio | -0.8352 |
| max_drawdown | 0.6437 |
| cagr | -0.3170 |
| net_avg_win | 48.3285 |
| net_avg_loss | -72.3904 |
| avg_hold_time_bars | 5.4518 |
| exposure | 0.1157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
