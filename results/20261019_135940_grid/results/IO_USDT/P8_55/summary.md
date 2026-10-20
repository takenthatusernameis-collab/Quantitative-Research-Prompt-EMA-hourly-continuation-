# EMA Hourly Continuation — IO/USDT P8_55

**Symbol:** IO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 994 |
| net_profit_factor | 0.6586 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 0.9194 |
| gross_win_rate | 0.4678 |
| sharpe_ratio | -5.1474 |
| sortino_ratio | -2.3632 |
| max_drawdown | 0.9324 |
| cagr | -0.6734 |
| net_avg_win | 39.0157 |
| net_avg_loss | -50.8287 |
| avg_hold_time_bars | 10.3028 |
| exposure | 0.4958 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
