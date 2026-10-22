# EMA Hourly Continuation — XCH/USDT P12_89

**Symbol:** XCH/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 568 |
| net_profit_factor | 0.8258 |
| net_win_rate | 0.5070 |
| gross_profit_factor | 1.0189 |
| gross_win_rate | 0.5070 |
| sharpe_ratio | -1.3451 |
| sortino_ratio | -0.4597 |
| max_drawdown | 0.4247 |
| cagr | -0.1934 |
| net_avg_win | 68.6753 |
| net_avg_loss | -85.5363 |
| avg_hold_time_bars | 21.0387 |
| exposure | 0.5432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
