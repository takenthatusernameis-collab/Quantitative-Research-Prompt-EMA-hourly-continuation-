# EMA Hourly Continuation — MANTA/USDT P50_89

**Symbol:** MANTA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.4993 |
| net_win_rate | 0.4425 |
| gross_profit_factor | 0.8275 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -5.6447 |
| sortino_ratio | -2.0679 |
| max_drawdown | 0.9180 |
| cagr | -0.6287 |
| net_avg_win | 30.8964 |
| net_avg_loss | -49.1005 |
| avg_hold_time_bars | 5.3752 |
| exposure | 0.1635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
