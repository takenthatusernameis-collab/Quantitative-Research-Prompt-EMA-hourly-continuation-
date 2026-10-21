# EMA Hourly Continuation — BOME/USDT P12_20

**Symbol:** BOME/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.7193 |
| net_win_rate | 0.4869 |
| gross_profit_factor | 0.9480 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -1.7094 |
| sortino_ratio | -0.3998 |
| max_drawdown | 0.4046 |
| cagr | -0.1679 |
| net_avg_win | 72.8690 |
| net_avg_loss | -96.1291 |
| avg_hold_time_bars | 4.3783 |
| exposure | 0.0531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
