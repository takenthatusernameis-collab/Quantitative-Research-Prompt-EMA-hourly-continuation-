# EMA Hourly Continuation — TAO/USDT P34_100

**Symbol:** TAO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.6336 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 0.9387 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -3.7629 |
| sortino_ratio | -1.3097 |
| max_drawdown | 0.7982 |
| cagr | -0.4699 |
| net_avg_win | 46.0837 |
| net_avg_loss | -68.3878 |
| avg_hold_time_bars | 9.2464 |
| exposure | 0.2593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
