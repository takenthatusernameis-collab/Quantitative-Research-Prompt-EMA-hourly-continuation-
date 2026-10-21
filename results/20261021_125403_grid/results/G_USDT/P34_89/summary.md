# EMA Hourly Continuation — G/USDT P34_89

**Symbol:** G/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.6030 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8272 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -3.5158 |
| sortino_ratio | -1.1160 |
| max_drawdown | 0.6941 |
| cagr | -0.4010 |
| net_avg_win | 52.2817 |
| net_avg_loss | -72.2549 |
| avg_hold_time_bars | 11.8392 |
| exposure | 0.2671 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
