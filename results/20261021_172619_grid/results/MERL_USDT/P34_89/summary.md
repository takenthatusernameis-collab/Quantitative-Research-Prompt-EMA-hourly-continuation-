# EMA Hourly Continuation — MERL/USDT P34_89

**Symbol:** MERL/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.8554 |
| net_win_rate | 0.5128 |
| gross_profit_factor | 1.0382 |
| gross_win_rate | 0.5128 |
| sharpe_ratio | -0.9618 |
| sortino_ratio | -0.2863 |
| max_drawdown | 0.3386 |
| cagr | -0.1259 |
| net_avg_win | 76.9576 |
| net_avg_loss | -94.6979 |
| avg_hold_time_bars | 11.3660 |
| exposure | 0.2223 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
