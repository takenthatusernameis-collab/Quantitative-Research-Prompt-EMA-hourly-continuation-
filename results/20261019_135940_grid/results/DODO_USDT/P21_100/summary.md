# EMA Hourly Continuation — DODO/USDT P21_100

**Symbol:** DODO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.5987 |
| net_win_rate | 0.4443 |
| gross_profit_factor | 0.9083 |
| gross_win_rate | 0.4542 |
| sharpe_ratio | -5.1714 |
| sortino_ratio | -1.9310 |
| max_drawdown | 0.9082 |
| cagr | -0.6027 |
| net_avg_win | 42.7408 |
| net_avg_loss | -57.0782 |
| avg_hold_time_bars | 13.6968 |
| exposure | 0.4394 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
