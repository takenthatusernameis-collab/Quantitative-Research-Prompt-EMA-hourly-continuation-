# EMA Hourly Continuation — STRAX/USDT P12_89

**Symbol:** STRAX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.6802 |
| net_win_rate | 0.4678 |
| gross_profit_factor | 0.8836 |
| gross_win_rate | 0.4678 |
| sharpe_ratio | -3.1914 |
| sortino_ratio | -1.1180 |
| max_drawdown | 0.7500 |
| cagr | -0.4032 |
| net_avg_win | 54.4418 |
| net_avg_loss | -70.3438 |
| avg_hold_time_bars | 17.6975 |
| exposure | 0.4895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
