# EMA Hourly Continuation — XAI/USDT P50_200

**Symbol:** XAI/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.8066 |
| net_win_rate | 0.4898 |
| gross_profit_factor | 0.9604 |
| gross_win_rate | 0.4898 |
| sharpe_ratio | -1.1718 |
| sortino_ratio | -0.2869 |
| max_drawdown | 0.3618 |
| cagr | -0.1249 |
| net_avg_win | 82.4409 |
| net_avg_loss | -98.1245 |
| avg_hold_time_bars | 33.8265 |
| exposure | 0.4520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
