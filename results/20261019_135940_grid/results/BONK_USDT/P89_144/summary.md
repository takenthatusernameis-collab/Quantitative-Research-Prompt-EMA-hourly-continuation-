# EMA Hourly Continuation — BONK/USDT P89_144

**Symbol:** BONK/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.5188 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.7907 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -4.6970 |
| sortino_ratio | -1.4690 |
| max_drawdown | 0.8446 |
| cagr | -0.5133 |
| net_avg_win | 40.9770 |
| net_avg_loss | -63.1837 |
| avg_hold_time_bars | 5.7798 |
| exposure | 0.1300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
