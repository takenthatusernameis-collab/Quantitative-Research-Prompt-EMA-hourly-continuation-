# EMA Hourly Continuation — KNC/USDT P55_89

**Symbol:** KNC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.6098 |
| net_win_rate | 0.4779 |
| gross_profit_factor | 0.9451 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -3.3271 |
| sortino_ratio | -0.9656 |
| max_drawdown | 0.6946 |
| cagr | -0.3556 |
| net_avg_win | 53.5561 |
| net_avg_loss | -80.4065 |
| avg_hold_time_bars | 6.5000 |
| exposure | 0.1205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
