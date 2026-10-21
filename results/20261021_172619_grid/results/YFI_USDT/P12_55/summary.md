# EMA Hourly Continuation — YFI/USDT P12_55

**Symbol:** YFI/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 750 |
| net_profit_factor | 0.5749 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.8568 |
| gross_win_rate | 0.4560 |
| sharpe_ratio | -4.8732 |
| sortino_ratio | -1.9028 |
| max_drawdown | 0.8923 |
| cagr | -0.5829 |
| net_avg_win | 35.1807 |
| net_avg_loss | -51.2995 |
| avg_hold_time_bars | 9.8573 |
| exposure | 0.3345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
