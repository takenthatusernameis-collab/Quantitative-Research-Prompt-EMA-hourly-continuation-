# EMA Hourly Continuation — AERO/USDT P144_200

**Symbol:** AERO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.5007 |
| net_win_rate | 0.4377 |
| gross_profit_factor | 0.8362 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -3.8959 |
| sortino_ratio | -1.0036 |
| max_drawdown | 0.7138 |
| cagr | -0.3805 |
| net_avg_win | 48.7193 |
| net_avg_loss | -75.7364 |
| avg_hold_time_bars | 4.3131 |
| exposure | 0.0645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
