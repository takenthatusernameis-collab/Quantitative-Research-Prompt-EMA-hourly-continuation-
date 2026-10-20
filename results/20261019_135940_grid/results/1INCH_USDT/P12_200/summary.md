# EMA Hourly Continuation — 1INCH/USDT P12_200

**Symbol:** 1INCH/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 203 |
| net_profit_factor | 0.6688 |
| net_win_rate | 0.4729 |
| gross_profit_factor | 0.9084 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -1.7295 |
| sortino_ratio | -0.3501 |
| max_drawdown | 0.3584 |
| cagr | -0.1497 |
| net_avg_win | 70.3750 |
| net_avg_loss | -94.4011 |
| avg_hold_time_bars | 91.9064 |
| exposure | 0.8480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
