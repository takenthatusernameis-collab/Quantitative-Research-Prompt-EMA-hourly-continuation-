# EMA Hourly Continuation — DEGEN/USDT P34_89

**Symbol:** DEGEN/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.8403 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 1.0193 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -1.2176 |
| sortino_ratio | -0.3632 |
| max_drawdown | 0.4064 |
| cagr | -0.1556 |
| net_avg_win | 83.3977 |
| net_avg_loss | -100.6324 |
| avg_hold_time_bars | 10.6028 |
| exposure | 0.2090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
