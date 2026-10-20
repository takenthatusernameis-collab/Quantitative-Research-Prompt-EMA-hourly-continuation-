# EMA Hourly Continuation — YGG/USDT P12_200

**Symbol:** YGG/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.7277 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9615 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -2.2848 |
| sortino_ratio | -0.6728 |
| max_drawdown | 0.5951 |
| cagr | -0.2716 |
| net_avg_win | 70.6988 |
| net_avg_loss | -88.6353 |
| avg_hold_time_bars | 35.8005 |
| exposure | 0.7063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
