# EMA Hourly Continuation — CETUS/USDT P12_55

**Symbol:** CETUS/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1039 |
| net_profit_factor | 0.6448 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.9873 |
| gross_win_rate | 0.4735 |
| sharpe_ratio | -5.8136 |
| sortino_ratio | -2.6207 |
| max_drawdown | 0.9627 |
| cagr | -0.7190 |
| net_avg_win | 36.2800 |
| net_avg_loss | -48.3144 |
| avg_hold_time_bars | 8.2560 |
| exposure | 0.3882 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
