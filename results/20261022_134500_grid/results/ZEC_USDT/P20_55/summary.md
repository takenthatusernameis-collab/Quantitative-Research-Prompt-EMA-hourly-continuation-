# EMA Hourly Continuation — ZEC/USDT P20_55

**Symbol:** ZEC/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 899 |
| net_profit_factor | 0.5159 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.9709 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -5.9632 |
| sortino_ratio | -2.5150 |
| max_drawdown | 0.9549 |
| cagr | -0.7071 |
| net_avg_win | 24.4432 |
| net_avg_loss | -40.8086 |
| avg_hold_time_bars | 5.5028 |
| exposure | 0.2249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
