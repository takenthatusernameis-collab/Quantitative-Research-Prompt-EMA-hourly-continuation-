# EMA Hourly Continuation — LSK/USDT P12_89

**Symbol:** LSK/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.6210 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 0.9388 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -4.0035 |
| sortino_ratio | -1.4211 |
| max_drawdown | 0.8314 |
| cagr | -0.4942 |
| net_avg_win | 45.2064 |
| net_avg_loss | -63.2196 |
| avg_hold_time_bars | 18.5039 |
| exposure | 0.5375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
