# EMA Hourly Continuation — XMR/USDT P12_100

**Symbol:** XMR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 990 |
| net_profit_factor | 0.4475 |
| net_win_rate | 0.4515 |
| gross_profit_factor | 0.8303 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -7.0687 |
| sortino_ratio | -3.1175 |
| max_drawdown | 0.9796 |
| cagr | -0.7862 |
| net_avg_win | 17.7427 |
| net_avg_loss | -32.6398 |
| avg_hold_time_bars | 11.3061 |
| exposure | 0.5088 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
