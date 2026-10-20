# EMA Hourly Continuation — IOST/USDT P55_89

**Symbol:** IOST/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.5106 |
| net_win_rate | 0.4802 |
| gross_profit_factor | 1.0761 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -5.8135 |
| sortino_ratio | -2.1029 |
| max_drawdown | 0.9283 |
| cagr | -0.6479 |
| net_avg_win | 30.7192 |
| net_avg_loss | -55.5709 |
| avg_hold_time_bars | 4.5579 |
| exposure | 0.1359 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
