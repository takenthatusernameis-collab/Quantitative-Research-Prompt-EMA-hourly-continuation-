# EMA Hourly Continuation — TIA/USDT P8_20

**Symbol:** TIA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1739 |
| net_profit_factor | 0.4213 |
| net_win_rate | 0.4393 |
| gross_profit_factor | 0.8132 |
| gross_win_rate | 0.4526 |
| sharpe_ratio | -11.0032 |
| sortino_ratio | -6.4707 |
| max_drawdown | 0.9997 |
| cagr | -0.9600 |
| net_avg_win | 9.5265 |
| net_avg_loss | -17.7182 |
| avg_hold_time_bars | 2.6072 |
| exposure | 0.2061 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
