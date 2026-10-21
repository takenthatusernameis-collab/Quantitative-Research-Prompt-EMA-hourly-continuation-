# EMA Hourly Continuation — SWFTC/USDT P34_144

**Symbol:** SWFTC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.7570 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 0.9435 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -1.6135 |
| sortino_ratio | -0.4146 |
| max_drawdown | 0.3841 |
| cagr | -0.1739 |
| net_avg_win | 75.5964 |
| net_avg_loss | -93.8858 |
| avg_hold_time_bars | 24.0988 |
| exposure | 0.3549 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
