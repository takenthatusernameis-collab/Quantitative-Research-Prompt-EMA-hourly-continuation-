# EMA Hourly Continuation — MOVR/USDT P89_100

**Symbol:** MOVR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 151 |
| net_profit_factor | 0.7934 |
| net_win_rate | 0.5364 |
| gross_profit_factor | 1.1479 |
| gross_win_rate | 0.5364 |
| sharpe_ratio | -0.8360 |
| sortino_ratio | -0.1486 |
| max_drawdown | 0.1894 |
| cagr | -0.0656 |
| net_avg_win | 74.2887 |
| net_avg_loss | -108.3505 |
| avg_hold_time_bars | 5.3377 |
| exposure | 0.0366 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
