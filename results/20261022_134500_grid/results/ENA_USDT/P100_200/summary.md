# EMA Hourly Continuation — ENA/USDT P100_200

**Symbol:** ENA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.7618 |
| net_win_rate | 0.5138 |
| gross_profit_factor | 1.0704 |
| gross_win_rate | 0.5193 |
| sharpe_ratio | -1.6153 |
| sortino_ratio | -0.4339 |
| max_drawdown | 0.4478 |
| cagr | -0.1871 |
| net_avg_win | 69.7190 |
| net_avg_loss | -96.7221 |
| avg_hold_time_bars | 7.7541 |
| exposure | 0.1276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
