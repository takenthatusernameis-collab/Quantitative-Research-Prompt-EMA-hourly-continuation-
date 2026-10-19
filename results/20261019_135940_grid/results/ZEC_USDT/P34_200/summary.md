# EMA Hourly Continuation — ZEC/USDT P34_200

**Symbol:** ZEC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.8355 |
| net_win_rate | 0.5234 |
| gross_profit_factor | 1.0934 |
| gross_win_rate | 0.5234 |
| sharpe_ratio | -0.9774 |
| sortino_ratio | -0.2646 |
| max_drawdown | 0.3280 |
| cagr | -0.1188 |
| net_avg_win | 72.7377 |
| net_avg_loss | -95.6186 |
| avg_hold_time_bars | 28.8733 |
| exposure | 0.4764 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
