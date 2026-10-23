# EMA Hourly Continuation — BIGTIME/USDT P8_144

**Symbol:** BIGTIME/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.8896 |
| net_win_rate | 0.5380 |
| gross_profit_factor | 1.1598 |
| gross_win_rate | 0.5380 |
| sharpe_ratio | -0.6376 |
| sortino_ratio | -0.1678 |
| max_drawdown | 0.2967 |
| cagr | -0.0789 |
| net_avg_win | 82.0138 |
| net_avg_loss | -107.3579 |
| avg_hold_time_bars | 51.9825 |
| exposure | 0.8045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
