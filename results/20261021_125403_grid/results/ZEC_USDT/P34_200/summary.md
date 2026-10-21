# EMA Hourly Continuation — ZEC/USDT P34_200

**Symbol:** ZEC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.9353 |
| net_win_rate | 0.5226 |
| gross_profit_factor | 1.0922 |
| gross_win_rate | 0.5226 |
| sharpe_ratio | -0.3066 |
| sortino_ratio | -0.0748 |
| max_drawdown | 0.1848 |
| cagr | -0.0378 |
| net_avg_win | 88.8745 |
| net_avg_loss | -104.0356 |
| avg_hold_time_bars | 36.0383 |
| exposure | 0.4701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
