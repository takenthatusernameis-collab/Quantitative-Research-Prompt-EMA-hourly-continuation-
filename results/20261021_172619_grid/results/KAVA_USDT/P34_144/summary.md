# EMA Hourly Continuation — KAVA/USDT P34_144

**Symbol:** KAVA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.7213 |
| net_win_rate | 0.4902 |
| gross_profit_factor | 1.0072 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.2752 |
| sortino_ratio | -0.6525 |
| max_drawdown | 0.5621 |
| cagr | -0.2638 |
| net_avg_win | 69.4394 |
| net_avg_loss | -92.5665 |
| avg_hold_time_bars | 20.9387 |
| exposure | 0.3883 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
