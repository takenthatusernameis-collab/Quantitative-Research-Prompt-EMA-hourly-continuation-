# EMA Hourly Continuation — SOL/USDT P12_20

**Symbol:** SOL/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 243 |
| net_profit_factor | 0.7695 |
| net_win_rate | 0.5350 |
| gross_profit_factor | 1.1436 |
| gross_win_rate | 0.5350 |
| sharpe_ratio | -1.2684 |
| sortino_ratio | -0.2863 |
| max_drawdown | 0.3120 |
| cagr | -0.1218 |
| net_avg_win | 71.4432 |
| net_avg_loss | -106.8136 |
| avg_hold_time_bars | 5.2305 |
| exposure | 0.0578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
