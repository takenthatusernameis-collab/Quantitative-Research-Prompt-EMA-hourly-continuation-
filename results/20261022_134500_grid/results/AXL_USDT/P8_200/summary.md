# EMA Hourly Continuation — AXL/USDT P8_200

**Symbol:** AXL/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.6615 |
| net_win_rate | 0.4634 |
| gross_profit_factor | 0.8904 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -3.0243 |
| sortino_ratio | -0.9004 |
| max_drawdown | 0.6853 |
| cagr | -0.3492 |
| net_avg_win | 61.8479 |
| net_avg_loss | -80.7518 |
| avg_hold_time_bars | 38.6984 |
| exposure | 0.7898 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
