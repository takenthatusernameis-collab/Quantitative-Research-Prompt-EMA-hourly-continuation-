# EMA Hourly Continuation — CSPR/USDT P8_89

**Symbol:** CSPR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.7291 |
| net_win_rate | 0.4712 |
| gross_profit_factor | 0.8868 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -2.2943 |
| sortino_ratio | -0.7697 |
| max_drawdown | 0.5975 |
| cagr | -0.2992 |
| net_avg_win | 60.6617 |
| net_avg_loss | -74.1444 |
| avg_hold_time_bars | 21.6960 |
| exposure | 0.5483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
