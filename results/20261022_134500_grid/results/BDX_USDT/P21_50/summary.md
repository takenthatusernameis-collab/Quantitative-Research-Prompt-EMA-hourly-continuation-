# EMA Hourly Continuation — BDX/USDT P21_50

**Symbol:** BDX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1382 |
| net_profit_factor | 0.2334 |
| net_win_rate | 0.2576 |
| gross_profit_factor | 0.6201 |
| gross_win_rate | 0.3234 |
| sharpe_ratio | -20.5129 |
| sortino_ratio | -11.7183 |
| max_drawdown | 1.0000 |
| cagr | -0.9986 |
| net_avg_win | 8.5529 |
| net_avg_loss | -12.7143 |
| avg_hold_time_bars | 3.5434 |
| exposure | 0.2226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
