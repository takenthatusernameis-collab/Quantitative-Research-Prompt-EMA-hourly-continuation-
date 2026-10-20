# EMA Hourly Continuation — SAFE/USDT P8_100

**Symbol:** SAFE/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.6079 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.9008 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -3.7836 |
| sortino_ratio | -1.3704 |
| max_drawdown | 0.8229 |
| cagr | -0.4842 |
| net_avg_win | 39.7736 |
| net_avg_loss | -58.8806 |
| avg_hold_time_bars | 21.3820 |
| exposure | 0.6512 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
