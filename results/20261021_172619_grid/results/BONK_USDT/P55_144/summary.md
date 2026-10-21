# EMA Hourly Continuation — BONK/USDT P55_144

**Symbol:** BONK/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.8038 |
| net_win_rate | 0.4937 |
| gross_profit_factor | 0.9620 |
| gross_win_rate | 0.4937 |
| sharpe_ratio | -1.1773 |
| sortino_ratio | -0.2991 |
| max_drawdown | 0.3648 |
| cagr | -0.1300 |
| net_avg_win | 77.4934 |
| net_avg_loss | -93.9976 |
| avg_hold_time_bars | 17.5063 |
| exposure | 0.2515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
