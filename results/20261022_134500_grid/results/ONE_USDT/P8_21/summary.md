# EMA Hourly Continuation — ONE/USDT P8_21

**Symbol:** ONE/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1653 |
| net_profit_factor | 0.3596 |
| net_win_rate | 0.4332 |
| gross_profit_factor | 0.7631 |
| gross_win_rate | 0.4471 |
| sharpe_ratio | -11.2016 |
| sortino_ratio | -6.4164 |
| max_drawdown | 0.9997 |
| cagr | -0.9596 |
| net_avg_win | 7.8393 |
| net_avg_loss | -16.6593 |
| avg_hold_time_bars | 3.1827 |
| exposure | 0.2391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
