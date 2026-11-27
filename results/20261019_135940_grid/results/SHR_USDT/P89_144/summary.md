# EMA Hourly Continuation — SHR/USDT P89_144

**Symbol:** SHR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.3699 |
| net_win_rate | 0.3031 |
| gross_profit_factor | 0.5523 |
| gross_win_rate | 0.3031 |
| sharpe_ratio | -9.2535 |
| sortino_ratio | -3.3878 |
| max_drawdown | 0.9857 |
| cagr | -0.8118 |
| net_avg_win | 27.9450 |
| net_avg_loss | -32.8501 |
| avg_hold_time_bars | 4.6999 |
| exposure | 0.1453 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
