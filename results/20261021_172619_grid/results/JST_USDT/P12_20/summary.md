# EMA Hourly Continuation — JST/USDT P12_20

**Symbol:** JST/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.4216 |
| net_win_rate | 0.5012 |
| gross_profit_factor | 1.0340 |
| gross_win_rate | 0.5315 |
| sharpe_ratio | -4.5641 |
| sortino_ratio | -1.3761 |
| max_drawdown | 0.7982 |
| cagr | -0.4683 |
| net_avg_win | 27.0136 |
| net_avg_loss | -64.3712 |
| avg_hold_time_bars | 5.0000 |
| exposure | 0.0971 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
