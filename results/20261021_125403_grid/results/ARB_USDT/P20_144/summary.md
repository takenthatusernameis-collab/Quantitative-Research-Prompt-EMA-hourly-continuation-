# EMA Hourly Continuation — ARB/USDT P20_144

**Symbol:** ARB/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.8701 |
| net_win_rate | 0.5123 |
| gross_profit_factor | 1.0522 |
| gross_win_rate | 0.5123 |
| sharpe_ratio | -0.8072 |
| sortino_ratio | -0.2085 |
| max_drawdown | 0.3179 |
| cagr | -0.0939 |
| net_avg_win | 88.4807 |
| net_avg_loss | -106.8375 |
| avg_hold_time_bars | 38.6574 |
| exposure | 0.5693 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
