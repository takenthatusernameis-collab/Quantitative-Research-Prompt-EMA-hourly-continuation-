# EMA Hourly Continuation — PYTH/USDT P21_89

**Symbol:** PYTH/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.7496 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.9100 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -2.0103 |
| sortino_ratio | -0.6268 |
| max_drawdown | 0.5398 |
| cagr | -0.2509 |
| net_avg_win | 67.7367 |
| net_avg_loss | -82.0816 |
| avg_hold_time_bars | 15.4530 |
| exposure | 0.3365 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
