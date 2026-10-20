# EMA Hourly Continuation — CTC/USDT P20_144

**Symbol:** CTC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.6075 |
| net_win_rate | 0.4673 |
| gross_profit_factor | 0.9587 |
| gross_win_rate | 0.4927 |
| sharpe_ratio | -3.7594 |
| sortino_ratio | -1.2337 |
| max_drawdown | 0.8023 |
| cagr | -0.4528 |
| net_avg_win | 46.9731 |
| net_avg_loss | -67.8221 |
| avg_hold_time_bars | 21.8091 |
| exposure | 0.5452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
