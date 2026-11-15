# EMA Hourly Continuation — CERE/USDT P20_55

**Symbol:** CERE/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1017 |
| net_profit_factor | 0.3696 |
| net_win_rate | 0.3333 |
| gross_profit_factor | 0.6952 |
| gross_win_rate | 0.3687 |
| sharpe_ratio | -12.8837 |
| sortino_ratio | -5.8628 |
| max_drawdown | 0.9996 |
| cagr | -0.9550 |
| net_avg_win | 17.2907 |
| net_avg_loss | -23.3885 |
| avg_hold_time_bars | 6.5133 |
| exposure | 0.3011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
