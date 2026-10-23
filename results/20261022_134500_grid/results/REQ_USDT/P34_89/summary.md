# EMA Hourly Continuation — REQ/USDT P34_89

**Symbol:** REQ/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 794 |
| net_profit_factor | 0.4659 |
| net_win_rate | 0.4232 |
| gross_profit_factor | 1.0004 |
| gross_win_rate | 0.4521 |
| sharpe_ratio | -8.4253 |
| sortino_ratio | -3.3430 |
| max_drawdown | 0.9872 |
| cagr | -0.8205 |
| net_avg_win | 25.6154 |
| net_avg_loss | -40.3337 |
| avg_hold_time_bars | 7.1020 |
| exposure | 0.2563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
