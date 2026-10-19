# EMA Hourly Continuation — LDO/USDT P34_100

**Symbol:** LDO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.5377 |
| net_win_rate | 0.4361 |
| gross_profit_factor | 0.7703 |
| gross_win_rate | 0.4470 |
| sharpe_ratio | -4.9163 |
| sortino_ratio | -1.7558 |
| max_drawdown | 0.8767 |
| cagr | -0.5639 |
| net_avg_win | 36.3661 |
| net_avg_loss | -52.3167 |
| avg_hold_time_bars | 9.7991 |
| exposure | 0.2860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
