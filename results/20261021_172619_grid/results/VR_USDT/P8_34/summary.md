# EMA Hourly Continuation — VR/USDT P8_34

**Symbol:** VR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.6974 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 0.9210 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -2.6686 |
| sortino_ratio | -0.8784 |
| max_drawdown | 0.6419 |
| cagr | -0.3356 |
| net_avg_win | 57.1126 |
| net_avg_loss | -76.0255 |
| avg_hold_time_bars | 13.5223 |
| exposure | 0.3307 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
