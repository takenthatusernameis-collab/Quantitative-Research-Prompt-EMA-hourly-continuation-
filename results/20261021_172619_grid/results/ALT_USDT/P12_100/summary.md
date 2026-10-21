# EMA Hourly Continuation — ALT/USDT P12_100

**Symbol:** ALT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.8253 |
| net_win_rate | 0.5010 |
| gross_profit_factor | 0.9994 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -1.3633 |
| sortino_ratio | -0.4375 |
| max_drawdown | 0.4728 |
| cagr | -0.1843 |
| net_avg_win | 75.0474 |
| net_avg_loss | -91.2978 |
| avg_hold_time_bars | 24.4394 |
| exposure | 0.5588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
