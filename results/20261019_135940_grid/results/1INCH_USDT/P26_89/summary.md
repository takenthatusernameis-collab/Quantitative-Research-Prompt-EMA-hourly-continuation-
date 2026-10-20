# EMA Hourly Continuation — 1INCH/USDT P26_89

**Symbol:** 1INCH/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 765 |
| net_profit_factor | 0.5187 |
| net_win_rate | 0.4418 |
| gross_profit_factor | 0.8768 |
| gross_win_rate | 0.4601 |
| sharpe_ratio | -6.2886 |
| sortino_ratio | -2.4558 |
| max_drawdown | 0.9509 |
| cagr | -0.6947 |
| net_avg_win | 30.2647 |
| net_avg_loss | -46.1858 |
| avg_hold_time_bars | 9.5712 |
| exposure | 0.3328 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
