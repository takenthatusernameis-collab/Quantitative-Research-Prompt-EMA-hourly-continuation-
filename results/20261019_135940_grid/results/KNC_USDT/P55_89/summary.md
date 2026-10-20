# EMA Hourly Continuation — KNC/USDT P55_89

**Symbol:** KNC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.4582 |
| net_win_rate | 0.4422 |
| gross_profit_factor | 0.9062 |
| gross_win_rate | 0.4739 |
| sharpe_ratio | -6.6123 |
| sortino_ratio | -2.3522 |
| max_drawdown | 0.9470 |
| cagr | -0.6867 |
| net_avg_win | 28.6704 |
| net_avg_loss | -49.5935 |
| avg_hold_time_bars | 4.8479 |
| exposure | 0.1390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
