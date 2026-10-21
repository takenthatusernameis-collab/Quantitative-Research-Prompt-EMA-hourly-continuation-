# EMA Hourly Continuation — BAND/USDT P89_144

**Symbol:** BAND/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.6103 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.8877 |
| gross_win_rate | 0.4735 |
| sharpe_ratio | -2.8368 |
| sortino_ratio | -0.7462 |
| max_drawdown | 0.5872 |
| cagr | -0.2907 |
| net_avg_win | 56.7328 |
| net_avg_loss | -82.6252 |
| avg_hold_time_bars | 6.5147 |
| exposure | 0.1002 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
