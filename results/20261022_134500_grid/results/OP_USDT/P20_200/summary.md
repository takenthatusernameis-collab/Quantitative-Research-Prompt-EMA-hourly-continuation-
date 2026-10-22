# EMA Hourly Continuation — OP/USDT P20_200

**Symbol:** OP/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.6262 |
| net_win_rate | 0.4591 |
| gross_profit_factor | 0.8651 |
| gross_win_rate | 0.4678 |
| sharpe_ratio | -2.6205 |
| sortino_ratio | -0.6792 |
| max_drawdown | 0.5576 |
| cagr | -0.2767 |
| net_avg_win | 59.3878 |
| net_avg_loss | -80.4878 |
| avg_hold_time_bars | 42.0673 |
| exposure | 0.6540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
