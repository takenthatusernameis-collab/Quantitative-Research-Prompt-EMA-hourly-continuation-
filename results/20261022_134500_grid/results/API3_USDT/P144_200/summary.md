# EMA Hourly Continuation — API3/USDT P144_200

**Symbol:** API3/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.5517 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.8978 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -4.0734 |
| sortino_ratio | -1.2098 |
| max_drawdown | 0.7634 |
| cagr | -0.4348 |
| net_avg_win | 46.6120 |
| net_avg_loss | -72.8890 |
| avg_hold_time_bars | 4.5922 |
| exposure | 0.0906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
