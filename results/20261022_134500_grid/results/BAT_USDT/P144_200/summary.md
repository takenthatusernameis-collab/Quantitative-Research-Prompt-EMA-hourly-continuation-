# EMA Hourly Continuation — BAT/USDT P144_200

**Symbol:** BAT/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.3794 |
| net_win_rate | 0.4455 |
| gross_profit_factor | 0.7804 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -5.0310 |
| sortino_ratio | -1.4761 |
| max_drawdown | 0.8347 |
| cagr | -0.5083 |
| net_avg_win | 27.0528 |
| net_avg_loss | -57.2817 |
| avg_hold_time_bars | 4.3815 |
| exposure | 0.0840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
