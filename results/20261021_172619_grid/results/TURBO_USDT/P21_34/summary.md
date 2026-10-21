# EMA Hourly Continuation — TURBO/USDT P21_34

**Symbol:** TURBO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 0.7992 |
| net_win_rate | 0.5156 |
| gross_profit_factor | 1.0603 |
| gross_win_rate | 0.5156 |
| sharpe_ratio | -1.2539 |
| sortino_ratio | -0.3163 |
| max_drawdown | 0.3363 |
| cagr | -0.1354 |
| net_avg_win | 79.1154 |
| net_avg_loss | -105.3831 |
| avg_hold_time_bars | 4.7070 |
| exposure | 0.0657 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
