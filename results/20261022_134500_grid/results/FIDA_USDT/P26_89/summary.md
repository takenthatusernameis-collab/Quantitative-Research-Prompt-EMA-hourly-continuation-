# EMA Hourly Continuation — FIDA/USDT P26_89

**Symbol:** FIDA/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 699 |
| net_profit_factor | 0.5467 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.8633 |
| gross_win_rate | 0.4721 |
| sharpe_ratio | -4.6999 |
| sortino_ratio | -1.7489 |
| max_drawdown | 0.8829 |
| cagr | -0.5654 |
| net_avg_win | 32.8729 |
| net_avg_loss | -51.3609 |
| avg_hold_time_bars | 10.3705 |
| exposure | 0.3280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
