# EMA Hourly Continuation — CTC/USDT P8_20

**Symbol:** CTC/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.5922 |
| net_win_rate | 0.4798 |
| gross_profit_factor | 0.8857 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -3.6399 |
| sortino_ratio | -1.2715 |
| max_drawdown | 0.7677 |
| cagr | -0.4408 |
| net_avg_win | 39.1256 |
| net_avg_loss | -60.9318 |
| avg_hold_time_bars | 6.3889 |
| exposure | 0.1725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
