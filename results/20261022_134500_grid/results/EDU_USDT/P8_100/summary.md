# EMA Hourly Continuation — EDU/USDT P8_100

**Symbol:** EDU/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.6338 |
| net_win_rate | 0.4556 |
| gross_profit_factor | 0.8649 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -4.0280 |
| sortino_ratio | -1.5080 |
| max_drawdown | 0.8411 |
| cagr | -0.5092 |
| net_avg_win | 44.6807 |
| net_avg_loss | -58.9939 |
| avg_hold_time_bars | 20.9252 |
| exposure | 0.6713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
