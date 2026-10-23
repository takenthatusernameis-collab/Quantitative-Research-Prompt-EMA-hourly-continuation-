# EMA Hourly Continuation — CYBER/USDT P26_89

**Symbol:** CYBER/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 710 |
| net_profit_factor | 0.6213 |
| net_win_rate | 0.4845 |
| gross_profit_factor | 0.9678 |
| gross_win_rate | 0.4944 |
| sharpe_ratio | -3.8465 |
| sortino_ratio | -1.4543 |
| max_drawdown | 0.8299 |
| cagr | -0.4919 |
| net_avg_win | 38.9771 |
| net_avg_loss | -58.9677 |
| avg_hold_time_bars | 10.3718 |
| exposure | 0.3347 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
