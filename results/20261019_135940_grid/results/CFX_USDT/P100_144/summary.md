# EMA Hourly Continuation — CFX/USDT P100_144

**Symbol:** CFX/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.4703 |
| net_win_rate | 0.4534 |
| gross_profit_factor | 0.8603 |
| gross_win_rate | 0.4555 |
| sharpe_ratio | -5.1203 |
| sortino_ratio | -1.5390 |
| max_drawdown | 0.8576 |
| cagr | -0.5390 |
| net_avg_win | 36.4075 |
| net_avg_loss | -64.2014 |
| avg_hold_time_bars | 4.0174 |
| exposure | 0.0842 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
