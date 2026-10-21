# EMA Hourly Continuation — RUNE/USDT P8_34

**Symbol:** RUNE/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.7243 |
| net_win_rate | 0.4848 |
| gross_profit_factor | 0.9566 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -2.9590 |
| sortino_ratio | -1.1100 |
| max_drawdown | 0.7394 |
| cagr | -0.3990 |
| net_avg_win | 56.7443 |
| net_avg_loss | -73.7138 |
| avg_hold_time_bars | 9.1959 |
| exposure | 0.2880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
