# EMA Hourly Continuation — XCH/USDT P34_89

**Symbol:** XCH/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.7492 |
| net_win_rate | 0.4936 |
| gross_profit_factor | 0.9642 |
| gross_win_rate | 0.4936 |
| sharpe_ratio | -1.8611 |
| sortino_ratio | -0.5788 |
| max_drawdown | 0.4972 |
| cagr | -0.2341 |
| net_avg_win | 62.5901 |
| net_avg_loss | -81.4415 |
| avg_hold_time_bars | 11.5763 |
| exposure | 0.2484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
