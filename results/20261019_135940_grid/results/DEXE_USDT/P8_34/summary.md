# EMA Hourly Continuation — DEXE/USDT P8_34

**Symbol:** DEXE/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1333 |
| net_profit_factor | 0.3840 |
| net_win_rate | 0.4254 |
| gross_profit_factor | 0.7062 |
| gross_win_rate | 0.4389 |
| sharpe_ratio | -9.4072 |
| sortino_ratio | -4.8368 |
| max_drawdown | 0.9976 |
| cagr | -0.9089 |
| net_avg_win | 10.9679 |
| net_avg_loss | -21.1416 |
| avg_hold_time_bars | 7.1800 |
| exposure | 0.4350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
