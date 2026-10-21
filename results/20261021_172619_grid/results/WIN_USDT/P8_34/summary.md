# EMA Hourly Continuation — WIN/USDT P8_34

**Symbol:** WIN/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.6709 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 1.0013 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -3.4291 |
| sortino_ratio | -1.2892 |
| max_drawdown | 0.7768 |
| cagr | -0.4449 |
| net_avg_win | 46.5701 |
| net_avg_loss | -67.6096 |
| avg_hold_time_bars | 10.0599 |
| exposure | 0.3132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
