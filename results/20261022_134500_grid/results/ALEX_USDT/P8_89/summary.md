# EMA Hourly Continuation — ALEX/USDT P8_89

**Symbol:** ALEX/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.5929 |
| net_win_rate | 0.4397 |
| gross_profit_factor | 0.8890 |
| gross_win_rate | 0.4521 |
| sharpe_ratio | -4.3030 |
| sortino_ratio | -1.4295 |
| max_drawdown | 0.8331 |
| cagr | -0.4977 |
| net_avg_win | 48.3053 |
| net_avg_loss | -63.9410 |
| avg_hold_time_bars | 26.4539 |
| exposure | 0.6782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
