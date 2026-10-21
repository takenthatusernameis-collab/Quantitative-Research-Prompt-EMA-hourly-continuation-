# EMA Hourly Continuation — JTO/USDT P34_200

**Symbol:** JTO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.7642 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.8847 |
| gross_win_rate | 0.4727 |
| sharpe_ratio | -1.3988 |
| sortino_ratio | -0.3507 |
| max_drawdown | 0.3873 |
| cagr | -0.1495 |
| net_avg_win | 73.6850 |
| net_avg_loss | -86.4228 |
| avg_hold_time_bars | 32.6302 |
| exposure | 0.4613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
