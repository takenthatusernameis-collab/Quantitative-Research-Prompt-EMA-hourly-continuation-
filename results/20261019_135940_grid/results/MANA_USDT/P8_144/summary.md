# EMA Hourly Continuation — MANA/USDT P8_144

**Symbol:** MANA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.6076 |
| net_win_rate | 0.4800 |
| gross_profit_factor | 0.9498 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -2.6825 |
| sortino_ratio | -0.6983 |
| max_drawdown | 0.6039 |
| cagr | -0.2905 |
| net_avg_win | 53.2348 |
| net_avg_loss | -80.8789 |
| avg_hold_time_bars | 50.4743 |
| exposure | 0.8030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
