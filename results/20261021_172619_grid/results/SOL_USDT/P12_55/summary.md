# EMA Hourly Continuation — SOL/USDT P12_55

**Symbol:** SOL/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 625 |
| net_profit_factor | 0.7528 |
| net_win_rate | 0.5024 |
| gross_profit_factor | 1.0050 |
| gross_win_rate | 0.5024 |
| sharpe_ratio | -2.3191 |
| sortino_ratio | -0.8315 |
| max_drawdown | 0.6284 |
| cagr | -0.3167 |
| net_avg_win | 59.7273 |
| net_avg_loss | -80.1022 |
| avg_hold_time_bars | 10.8160 |
| exposure | 0.3073 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
