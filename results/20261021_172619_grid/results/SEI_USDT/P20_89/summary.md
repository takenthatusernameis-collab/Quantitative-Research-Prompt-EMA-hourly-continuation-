# EMA Hourly Continuation — SEI/USDT P20_89

**Symbol:** SEI/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.9046 |
| net_win_rate | 0.5247 |
| gross_profit_factor | 1.0954 |
| gross_win_rate | 0.5247 |
| sharpe_ratio | -0.6313 |
| sortino_ratio | -0.1922 |
| max_drawdown | 0.2789 |
| cagr | -0.0890 |
| net_avg_win | 84.5495 |
| net_avg_loss | -103.1639 |
| avg_hold_time_bars | 20.1435 |
| exposure | 0.4084 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
