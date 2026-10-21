# EMA Hourly Continuation — BONK/USDT P12_20

**Symbol:** BONK/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 247 |
| net_profit_factor | 0.8419 |
| net_win_rate | 0.5223 |
| gross_profit_factor | 1.0896 |
| gross_win_rate | 0.5223 |
| sharpe_ratio | -0.8495 |
| sortino_ratio | -0.1924 |
| max_drawdown | 0.2941 |
| cagr | -0.0857 |
| net_avg_win | 83.1937 |
| net_avg_loss | -108.0282 |
| avg_hold_time_bars | 5.4049 |
| exposure | 0.0607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
