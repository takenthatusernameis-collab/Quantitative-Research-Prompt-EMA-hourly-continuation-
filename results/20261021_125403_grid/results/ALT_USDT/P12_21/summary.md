# EMA Hourly Continuation — ALT/USDT P12_21

**Symbol:** ALT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 546 |
| net_profit_factor | 0.6288 |
| net_win_rate | 0.4707 |
| gross_profit_factor | 0.8853 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -3.4239 |
| sortino_ratio | -1.1437 |
| max_drawdown | 0.7398 |
| cagr | -0.4087 |
| net_avg_win | 48.2845 |
| net_avg_loss | -68.2910 |
| avg_hold_time_bars | 5.5495 |
| exposure | 0.1377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
