# EMA Hourly Continuation — G/USDT P20_89

**Symbol:** G/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.6001 |
| net_win_rate | 0.4442 |
| gross_profit_factor | 0.7803 |
| gross_win_rate | 0.4442 |
| sharpe_ratio | -3.3500 |
| sortino_ratio | -1.0378 |
| max_drawdown | 0.6728 |
| cagr | -0.3802 |
| net_avg_win | 52.9585 |
| net_avg_loss | -70.5278 |
| avg_hold_time_bars | 21.2015 |
| exposure | 0.4593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
