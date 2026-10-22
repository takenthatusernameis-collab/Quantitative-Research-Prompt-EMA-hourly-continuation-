# EMA Hourly Continuation — XCH/USDT P55_89

**Symbol:** XCH/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.6304 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.8542 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -2.2150 |
| sortino_ratio | -0.5330 |
| max_drawdown | 0.4611 |
| cagr | -0.2169 |
| net_avg_win | 58.8316 |
| net_avg_loss | -82.2007 |
| avg_hold_time_bars | 8.0458 |
| exposure | 0.1039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
