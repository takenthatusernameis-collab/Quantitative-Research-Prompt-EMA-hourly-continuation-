# EMA Hourly Continuation — AXL/USDT P34_200

**Symbol:** AXL/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.6990 |
| net_win_rate | 0.4742 |
| gross_profit_factor | 0.9394 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -2.5558 |
| sortino_ratio | -0.7556 |
| max_drawdown | 0.6023 |
| cagr | -0.3014 |
| net_avg_win | 65.5296 |
| net_avg_loss | -84.5350 |
| avg_hold_time_bars | 25.0876 |
| exposure | 0.5052 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
