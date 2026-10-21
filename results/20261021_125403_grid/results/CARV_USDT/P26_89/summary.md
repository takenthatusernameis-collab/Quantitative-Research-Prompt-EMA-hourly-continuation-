# EMA Hourly Continuation — CARV/USDT P26_89

**Symbol:** CARV/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.6417 |
| net_win_rate | 0.4494 |
| gross_profit_factor | 0.8171 |
| gross_win_rate | 0.4494 |
| sharpe_ratio | -3.0743 |
| sortino_ratio | -0.9528 |
| max_drawdown | 0.6140 |
| cagr | -0.3549 |
| net_avg_win | 60.9833 |
| net_avg_loss | -77.5493 |
| avg_hold_time_bars | 13.7117 |
| exposure | 0.2971 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
