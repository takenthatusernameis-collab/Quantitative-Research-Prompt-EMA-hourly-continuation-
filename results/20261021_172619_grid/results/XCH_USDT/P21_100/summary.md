# EMA Hourly Continuation — XCH/USDT P21_100

**Symbol:** XCH/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.8580 |
| net_win_rate | 0.5203 |
| gross_profit_factor | 1.0709 |
| gross_win_rate | 0.5203 |
| sharpe_ratio | -0.9792 |
| sortino_ratio | -0.3204 |
| max_drawdown | 0.3623 |
| cagr | -0.1402 |
| net_avg_win | 70.9207 |
| net_avg_loss | -89.6572 |
| avg_hold_time_bars | 18.4487 |
| exposure | 0.4335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
