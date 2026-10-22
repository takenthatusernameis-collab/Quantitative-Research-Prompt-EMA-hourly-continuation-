# EMA Hourly Continuation — FIL/USDT P26_89

**Symbol:** FIL/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.5098 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.8432 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -5.5677 |
| sortino_ratio | -2.0495 |
| max_drawdown | 0.9222 |
| cagr | -0.6284 |
| net_avg_win | 31.3646 |
| net_avg_loss | -49.2172 |
| avg_hold_time_bars | 10.1199 |
| exposure | 0.3146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
