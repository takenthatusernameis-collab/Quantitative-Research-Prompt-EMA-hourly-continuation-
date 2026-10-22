# EMA Hourly Continuation — XTZ/USDT P20_200

**Symbol:** XTZ/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.6262 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.9488 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -2.8438 |
| sortino_ratio | -0.7790 |
| max_drawdown | 0.6210 |
| cagr | -0.3127 |
| net_avg_win | 56.1618 |
| net_avg_loss | -81.6114 |
| avg_hold_time_bars | 38.4581 |
| exposure | 0.6678 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
