# EMA Hourly Continuation — MANA/USDT P20_89

**Symbol:** MANA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 729 |
| net_profit_factor | 0.5913 |
| net_win_rate | 0.4417 |
| gross_profit_factor | 0.9500 |
| gross_win_rate | 0.4540 |
| sharpe_ratio | -5.9301 |
| sortino_ratio | -2.2338 |
| max_drawdown | 0.9427 |
| cagr | -0.6711 |
| net_avg_win | 42.1707 |
| net_avg_loss | -56.4286 |
| avg_hold_time_bars | 11.4774 |
| exposure | 0.3803 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
