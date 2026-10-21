# EMA Hourly Continuation — STRK/USDT P12_89

**Symbol:** STRK/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.8791 |
| net_win_rate | 0.5159 |
| gross_profit_factor | 1.0530 |
| gross_win_rate | 0.5159 |
| sharpe_ratio | -0.8272 |
| sortino_ratio | -0.2584 |
| max_drawdown | 0.3194 |
| cagr | -0.1157 |
| net_avg_win | 79.1311 |
| net_avg_loss | -95.9142 |
| avg_hold_time_bars | 25.3256 |
| exposure | 0.5445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
