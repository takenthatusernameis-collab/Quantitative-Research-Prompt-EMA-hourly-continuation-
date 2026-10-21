# EMA Hourly Continuation — CELO/USDT P12_89

**Symbol:** CELO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.8734 |
| net_win_rate | 0.5166 |
| gross_profit_factor | 1.0752 |
| gross_win_rate | 0.5166 |
| sharpe_ratio | -1.0444 |
| sortino_ratio | -0.3488 |
| max_drawdown | 0.4178 |
| cagr | -0.1515 |
| net_avg_win | 83.5625 |
| net_avg_loss | -102.2535 |
| avg_hold_time_bars | 22.3893 |
| exposure | 0.5491 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
