# EMA Hourly Continuation — TRX/USDT P8_21

**Symbol:** TRX/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1422 |
| net_profit_factor | 0.1046 |
| net_win_rate | 0.2834 |
| gross_profit_factor | 0.7972 |
| gross_win_rate | 0.4367 |
| sharpe_ratio | -20.4082 |
| sortino_ratio | -12.1403 |
| max_drawdown | 1.0000 |
| cagr | -0.9988 |
| net_avg_win | 2.9002 |
| net_avg_loss | -10.9605 |
| avg_hold_time_bars | 3.5105 |
| exposure | 0.2269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
