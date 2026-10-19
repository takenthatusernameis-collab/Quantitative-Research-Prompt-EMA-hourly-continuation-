# EMA Hourly Continuation — RAY/USDT P26_55

**Symbol:** RAY/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 858 |
| net_profit_factor | 0.5824 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.9415 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -5.3884 |
| sortino_ratio | -2.2134 |
| max_drawdown | 0.9411 |
| cagr | -0.6618 |
| net_avg_win | 31.9413 |
| net_avg_loss | -49.7219 |
| avg_hold_time_bars | 4.4790 |
| exposure | 0.1747 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
