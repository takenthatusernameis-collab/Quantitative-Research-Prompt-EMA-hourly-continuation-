# EMA Hourly Continuation — FIDA/USDT P20_89

**Symbol:** FIDA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 700 |
| net_profit_factor | 0.5306 |
| net_win_rate | 0.4514 |
| gross_profit_factor | 0.8222 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -4.7024 |
| sortino_ratio | -1.7527 |
| max_drawdown | 0.8835 |
| cagr | -0.5625 |
| net_avg_win | 31.3258 |
| net_avg_loss | -48.5842 |
| avg_hold_time_bars | 12.8129 |
| exposure | 0.4059 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
