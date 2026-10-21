# EMA Hourly Continuation — XCH/USDT P89_100

**Symbol:** XCH/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 102 |
| net_profit_factor | 0.5083 |
| net_win_rate | 0.4216 |
| gross_profit_factor | 0.7189 |
| gross_win_rate | 0.4216 |
| sharpe_ratio | -2.0363 |
| sortino_ratio | -0.2929 |
| max_drawdown | 0.2901 |
| cagr | -0.1262 |
| net_avg_win | 69.0706 |
| net_avg_loss | -99.0424 |
| avg_hold_time_bars | 5.2647 |
| exposure | 0.0244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
