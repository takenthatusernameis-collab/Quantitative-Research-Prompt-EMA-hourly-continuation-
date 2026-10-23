# EMA Hourly Continuation — WOO/USDT P20_100

**Symbol:** WOO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.7050 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 1.0100 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -3.5017 |
| sortino_ratio | -1.2253 |
| max_drawdown | 0.7941 |
| cagr | -0.4377 |
| net_avg_win | 63.4208 |
| net_avg_loss | -79.9684 |
| avg_hold_time_bars | 15.8905 |
| exposure | 0.4420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
