# EMA Hourly Continuation — QNT/USDT P8_144

**Symbol:** QNT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.8249 |
| net_win_rate | 0.5111 |
| gross_profit_factor | 1.0285 |
| gross_win_rate | 0.5111 |
| sharpe_ratio | -1.2499 |
| sortino_ratio | -0.3993 |
| max_drawdown | 0.4165 |
| cagr | -0.1697 |
| net_avg_win | 69.4886 |
| net_avg_loss | -88.0671 |
| avg_hold_time_bars | 29.3192 |
| exposure | 0.6597 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
