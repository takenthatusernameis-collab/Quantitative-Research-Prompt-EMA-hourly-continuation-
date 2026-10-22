# EMA Hourly Continuation — JST/USDT P12_21

**Symbol:** JST/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1191 |
| net_profit_factor | 0.1011 |
| net_win_rate | 0.3543 |
| gross_profit_factor | 0.6332 |
| gross_win_rate | 0.4517 |
| sharpe_ratio | -15.6480 |
| sortino_ratio | -8.0387 |
| max_drawdown | 1.0000 |
| cagr | -0.9877 |
| net_avg_win | 2.6658 |
| net_avg_loss | -14.4666 |
| avg_hold_time_bars | 3.0411 |
| exposure | 0.1639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
