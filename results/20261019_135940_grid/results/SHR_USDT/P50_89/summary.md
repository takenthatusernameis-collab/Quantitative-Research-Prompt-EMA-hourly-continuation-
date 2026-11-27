# EMA Hourly Continuation — SHR/USDT P50_89

**Symbol:** SHR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 881 |
| net_profit_factor | 0.3687 |
| net_win_rate | 0.3235 |
| gross_profit_factor | 0.5502 |
| gross_win_rate | 0.3246 |
| sharpe_ratio | -9.8656 |
| sortino_ratio | -4.1122 |
| max_drawdown | 0.9935 |
| cagr | -0.8636 |
| net_avg_win | 20.3558 |
| net_avg_loss | -26.4022 |
| avg_hold_time_bars | 4.0908 |
| exposure | 0.1631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
