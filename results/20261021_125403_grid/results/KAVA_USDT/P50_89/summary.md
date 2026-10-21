# EMA Hourly Continuation — KAVA/USDT P50_89

**Symbol:** KAVA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.5101 |
| net_win_rate | 0.4310 |
| gross_profit_factor | 0.7774 |
| gross_win_rate | 0.4334 |
| sharpe_ratio | -4.6630 |
| sortino_ratio | -1.3507 |
| max_drawdown | 0.8100 |
| cagr | -0.4720 |
| net_avg_win | 46.7265 |
| net_avg_loss | -69.3888 |
| avg_hold_time_bars | 8.0484 |
| exposure | 0.1511 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
