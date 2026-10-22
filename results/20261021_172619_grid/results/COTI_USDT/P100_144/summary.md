# EMA Hourly Continuation — COTI/USDT P100_144

**Symbol:** COTI/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 218 |
| net_profit_factor | 0.7538 |
| net_win_rate | 0.5092 |
| gross_profit_factor | 1.0050 |
| gross_win_rate | 0.5092 |
| sharpe_ratio | -1.1679 |
| sortino_ratio | -0.2480 |
| max_drawdown | 0.2929 |
| cagr | -0.1075 |
| net_avg_win | 68.5506 |
| net_avg_loss | -94.3397 |
| avg_hold_time_bars | 5.9817 |
| exposure | 0.0593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
