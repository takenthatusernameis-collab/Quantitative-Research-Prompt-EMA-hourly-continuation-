# EMA Hourly Continuation — DODO/USDT P12_89

**Symbol:** DODO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 822 |
| net_profit_factor | 0.6112 |
| net_win_rate | 0.4489 |
| gross_profit_factor | 0.9033 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -5.1114 |
| sortino_ratio | -2.0576 |
| max_drawdown | 0.9231 |
| cagr | -0.6250 |
| net_avg_win | 39.0202 |
| net_avg_loss | -52.0009 |
| avg_hold_time_bars | 13.7324 |
| exposure | 0.5108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
