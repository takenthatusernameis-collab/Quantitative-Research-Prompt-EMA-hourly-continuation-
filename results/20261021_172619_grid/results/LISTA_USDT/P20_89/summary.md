# EMA Hourly Continuation — LISTA/USDT P20_89

**Symbol:** LISTA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.8303 |
| net_win_rate | 0.4957 |
| gross_profit_factor | 1.0057 |
| gross_win_rate | 0.4957 |
| sharpe_ratio | -1.4807 |
| sortino_ratio | -0.4758 |
| max_drawdown | 0.4581 |
| cagr | -0.1984 |
| net_avg_win | 84.6700 |
| net_avg_loss | -100.2527 |
| avg_hold_time_bars | 17.1319 |
| exposure | 0.3937 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
