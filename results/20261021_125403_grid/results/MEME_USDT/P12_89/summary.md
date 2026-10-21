# EMA Hourly Continuation — MEME/USDT P12_89

**Symbol:** MEME/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.7872 |
| net_win_rate | 0.4871 |
| gross_profit_factor | 0.9524 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -1.7024 |
| sortino_ratio | -0.5243 |
| max_drawdown | 0.4976 |
| cagr | -0.2158 |
| net_avg_win | 74.4531 |
| net_avg_loss | -89.8318 |
| avg_hold_time_bars | 27.2639 |
| exposure | 0.5775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
