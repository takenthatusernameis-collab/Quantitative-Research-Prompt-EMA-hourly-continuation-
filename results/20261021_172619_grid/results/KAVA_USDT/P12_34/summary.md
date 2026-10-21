# EMA Hourly Continuation — KAVA/USDT P12_34

**Symbol:** KAVA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.6061 |
| net_win_rate | 0.4581 |
| gross_profit_factor | 0.9007 |
| gross_win_rate | 0.4612 |
| sharpe_ratio | -4.6534 |
| sortino_ratio | -1.6858 |
| max_drawdown | 0.8646 |
| cagr | -0.5428 |
| net_avg_win | 44.8526 |
| net_avg_loss | -62.5515 |
| avg_hold_time_bars | 8.3028 |
| exposure | 0.2430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
