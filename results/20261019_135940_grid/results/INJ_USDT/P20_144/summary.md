# EMA Hourly Continuation — INJ/USDT P20_144

**Symbol:** INJ/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.6880 |
| net_win_rate | 0.4817 |
| gross_profit_factor | 0.9534 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -2.7015 |
| sortino_ratio | -0.8419 |
| max_drawdown | 0.6398 |
| cagr | -0.3306 |
| net_avg_win | 59.0862 |
| net_avg_loss | -79.8169 |
| avg_hold_time_bars | 24.2907 |
| exposure | 0.5432 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
