# EMA Hourly Continuation — NEO/USDT P34_100

**Symbol:** NEO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 645 |
| net_profit_factor | 0.4776 |
| net_win_rate | 0.4481 |
| gross_profit_factor | 0.8397 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -5.5995 |
| sortino_ratio | -2.0043 |
| max_drawdown | 0.9146 |
| cagr | -0.6203 |
| net_avg_win | 28.8571 |
| net_avg_loss | -49.0470 |
| avg_hold_time_bars | 9.8558 |
| exposure | 0.2890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
