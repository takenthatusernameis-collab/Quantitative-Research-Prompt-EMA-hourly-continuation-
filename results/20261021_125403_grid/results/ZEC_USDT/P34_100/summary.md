# EMA Hourly Continuation — ZEC/USDT P34_100

**Symbol:** ZEC/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.9289 |
| net_win_rate | 0.5310 |
| gross_profit_factor | 1.1328 |
| gross_win_rate | 0.5310 |
| sharpe_ratio | -0.4547 |
| sortino_ratio | -0.1265 |
| max_drawdown | 0.3232 |
| cagr | -0.0606 |
| net_avg_win | 96.4309 |
| net_avg_loss | -117.5322 |
| avg_hold_time_bars | 12.5283 |
| exposure | 0.2113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
