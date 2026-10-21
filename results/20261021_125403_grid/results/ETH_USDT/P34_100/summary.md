# EMA Hourly Continuation — ETH/USDT P34_100

**Symbol:** ETH/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.6604 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 0.9541 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -2.2888 |
| sortino_ratio | -0.6137 |
| max_drawdown | 0.5261 |
| cagr | -0.2453 |
| net_avg_win | 56.9541 |
| net_avg_loss | -84.2987 |
| avg_hold_time_bars | 16.9971 |
| exposure | 0.2704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
