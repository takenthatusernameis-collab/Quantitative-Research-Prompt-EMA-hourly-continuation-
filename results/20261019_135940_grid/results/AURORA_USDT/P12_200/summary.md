# EMA Hourly Continuation — AURORA/USDT P12_200

**Symbol:** AURORA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.5675 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.8394 |
| gross_win_rate | 0.4520 |
| sharpe_ratio | -3.9590 |
| sortino_ratio | -1.1924 |
| max_drawdown | 0.7682 |
| cagr | -0.4349 |
| net_avg_win | 49.4736 |
| net_avg_loss | -68.7847 |
| avg_hold_time_bars | 31.0655 |
| exposure | 0.6467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
