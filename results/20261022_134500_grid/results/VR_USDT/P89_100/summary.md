# EMA Hourly Continuation — VR/USDT P89_100

**Symbol:** VR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.2123 |
| net_win_rate | 0.2496 |
| gross_profit_factor | 0.5186 |
| gross_win_rate | 0.2738 |
| sharpe_ratio | -13.8859 |
| sortino_ratio | -5.4547 |
| max_drawdown | 0.9997 |
| cagr | -0.9584 |
| net_avg_win | 16.3307 |
| net_avg_loss | -25.5870 |
| avg_hold_time_bars | 2.9546 |
| exposure | 0.0888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
