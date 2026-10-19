# EMA Hourly Continuation — ZEC/USDT P34_55

**Symbol:** ZEC/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 818 |
| net_profit_factor | 0.4293 |
| net_win_rate | 0.4389 |
| gross_profit_factor | 0.9903 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -7.6964 |
| sortino_ratio | -3.0852 |
| max_drawdown | 0.9812 |
| cagr | -0.7929 |
| net_avg_win | 20.5531 |
| net_avg_loss | -37.4441 |
| avg_hold_time_bars | 2.7592 |
| exposure | 0.1026 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
