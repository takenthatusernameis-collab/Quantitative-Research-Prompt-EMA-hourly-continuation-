# EMA Hourly Continuation — SAFE/USDT P12_100

**Symbol:** SAFE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 618 |
| net_profit_factor | 0.6130 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9061 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -3.5153 |
| sortino_ratio | -1.2238 |
| max_drawdown | 0.7897 |
| cagr | -0.4490 |
| net_avg_win | 41.4012 |
| net_avg_loss | -62.0849 |
| avg_hold_time_bars | 21.0275 |
| exposure | 0.5951 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
