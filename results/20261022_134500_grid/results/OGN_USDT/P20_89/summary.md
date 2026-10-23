# EMA Hourly Continuation — OGN/USDT P20_89

**Symbol:** OGN/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 727 |
| net_profit_factor | 0.5641 |
| net_win_rate | 0.4415 |
| gross_profit_factor | 0.9143 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -5.6375 |
| sortino_ratio | -2.1312 |
| max_drawdown | 0.9330 |
| cagr | -0.6428 |
| net_avg_win | 37.3146 |
| net_avg_loss | -52.2980 |
| avg_hold_time_bars | 11.9202 |
| exposure | 0.3921 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
