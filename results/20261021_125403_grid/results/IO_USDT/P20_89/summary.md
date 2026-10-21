# EMA Hourly Continuation — IO/USDT P20_89

**Symbol:** IO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.7957 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 0.9448 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -1.6108 |
| sortino_ratio | -0.5059 |
| max_drawdown | 0.4522 |
| cagr | -0.2088 |
| net_avg_win | 74.7815 |
| net_avg_loss | -88.7636 |
| avg_hold_time_bars | 17.3033 |
| exposure | 0.3811 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
