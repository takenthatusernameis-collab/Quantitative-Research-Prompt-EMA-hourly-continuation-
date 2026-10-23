# EMA Hourly Continuation — IO/USDT P20_100

**Symbol:** IO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.6203 |
| net_win_rate | 0.4653 |
| gross_profit_factor | 0.8889 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -4.1604 |
| sortino_ratio | -1.5493 |
| max_drawdown | 0.8348 |
| cagr | -0.5257 |
| net_avg_win | 43.9072 |
| net_avg_loss | -61.5845 |
| avg_hold_time_bars | 13.5710 |
| exposure | 0.4349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
