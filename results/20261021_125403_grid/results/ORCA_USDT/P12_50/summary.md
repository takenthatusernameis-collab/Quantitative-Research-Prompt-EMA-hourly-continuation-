# EMA Hourly Continuation — ORCA/USDT P12_50

**Symbol:** ORCA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 690 |
| net_profit_factor | 0.7997 |
| net_win_rate | 0.5130 |
| gross_profit_factor | 1.0505 |
| gross_win_rate | 0.5130 |
| sharpe_ratio | -1.9327 |
| sortino_ratio | -0.7278 |
| max_drawdown | 0.6262 |
| cagr | -0.2871 |
| net_avg_win | 64.5470 |
| net_avg_loss | -85.0423 |
| avg_hold_time_bars | 10.5029 |
| exposure | 0.3294 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
