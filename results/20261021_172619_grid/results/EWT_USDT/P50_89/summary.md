# EMA Hourly Continuation — EWT/USDT P50_89

**Symbol:** EWT/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.7406 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 0.9681 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -1.5618 |
| sortino_ratio | -0.3578 |
| max_drawdown | 0.3880 |
| cagr | -0.1525 |
| net_avg_win | 77.0406 |
| net_avg_loss | -100.0585 |
| avg_hold_time_bars | 8.4163 |
| exposure | 0.0983 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
