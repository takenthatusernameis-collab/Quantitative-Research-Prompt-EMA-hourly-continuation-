# EMA Hourly Continuation — PEOPLE/USDT P20_89

**Symbol:** PEOPLE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.7450 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9042 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -1.9814 |
| sortino_ratio | -0.6146 |
| max_drawdown | 0.5475 |
| cagr | -0.2463 |
| net_avg_win | 65.3322 |
| net_avg_loss | -80.6245 |
| avg_hold_time_bars | 19.5588 |
| exposure | 0.4213 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
