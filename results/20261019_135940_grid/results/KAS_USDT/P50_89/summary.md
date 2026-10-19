# EMA Hourly Continuation — KAS/USDT P50_89

**Symbol:** KAS/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 700 |
| net_profit_factor | 0.3653 |
| net_win_rate | 0.4257 |
| gross_profit_factor | 0.7673 |
| gross_win_rate | 0.4457 |
| sharpe_ratio | -7.3146 |
| sortino_ratio | -2.7387 |
| max_drawdown | 0.9678 |
| cagr | -0.7438 |
| net_avg_win | 18.6835 |
| net_avg_loss | -37.9117 |
| avg_hold_time_bars | 4.3500 |
| exposure | 0.1384 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
