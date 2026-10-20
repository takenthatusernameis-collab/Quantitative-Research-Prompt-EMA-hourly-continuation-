# EMA Hourly Continuation — ORBS/USDT P34_50

**Symbol:** ORBS/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 961 |
| net_profit_factor | 0.2800 |
| net_win_rate | 0.3486 |
| gross_profit_factor | 0.8341 |
| gross_win_rate | 0.3996 |
| sharpe_ratio | -12.5992 |
| sortino_ratio | -5.6515 |
| max_drawdown | 0.9994 |
| cagr | -0.9478 |
| net_avg_win | 11.5992 |
| net_avg_loss | -22.1721 |
| avg_hold_time_bars | 3.7586 |
| exposure | 0.1642 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
