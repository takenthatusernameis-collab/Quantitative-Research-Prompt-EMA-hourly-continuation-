# EMA Hourly Continuation — TRADE/USDT P34_100

**Symbol:** TRADE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 539 |
| net_profit_factor | 0.5359 |
| net_win_rate | 0.4230 |
| gross_profit_factor | 0.8004 |
| gross_win_rate | 0.4267 |
| sharpe_ratio | -5.0661 |
| sortino_ratio | -1.6533 |
| max_drawdown | 0.8730 |
| cagr | -0.5543 |
| net_avg_win | 43.9940 |
| net_avg_loss | -60.1817 |
| avg_hold_time_bars | 10.2171 |
| exposure | 0.2503 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
