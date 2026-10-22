# EMA Hourly Continuation — WAVES/USDT P89_144

**Symbol:** WAVES/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.7492 |
| net_win_rate | 0.5248 |
| gross_profit_factor | 1.1008 |
| gross_win_rate | 0.5248 |
| sharpe_ratio | -1.5519 |
| sortino_ratio | -0.3755 |
| max_drawdown | 0.3796 |
| cagr | -0.1588 |
| net_avg_win | 71.0836 |
| net_avg_loss | -104.7941 |
| avg_hold_time_bars | 7.9965 |
| exposure | 0.1025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
