# EMA Hourly Continuation — ATH/USDT P20_144

**Symbol:** ATH/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.9289 |
| net_win_rate | 0.5284 |
| gross_profit_factor | 1.1061 |
| gross_win_rate | 0.5284 |
| sharpe_ratio | -0.4052 |
| sortino_ratio | -0.1131 |
| max_drawdown | 0.1757 |
| cagr | -0.0554 |
| net_avg_win | 88.2011 |
| net_avg_loss | -106.3977 |
| avg_hold_time_bars | 31.7472 |
| exposure | 0.5417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
