# EMA Hourly Continuation — ATH/USDT P55_100

**Symbol:** ATH/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.7448 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 0.9522 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -1.5552 |
| sortino_ratio | -0.3934 |
| max_drawdown | 0.3618 |
| cagr | -0.1655 |
| net_avg_win | 70.2950 |
| net_avg_loss | -91.2188 |
| avg_hold_time_bars | 8.5836 |
| exposure | 0.1219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
