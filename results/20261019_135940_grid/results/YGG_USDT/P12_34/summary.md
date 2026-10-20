# EMA Hourly Continuation — YGG/USDT P12_34

**Symbol:** YGG/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1264 |
| net_profit_factor | 0.5376 |
| net_win_rate | 0.4248 |
| gross_profit_factor | 0.8449 |
| gross_win_rate | 0.4367 |
| sharpe_ratio | -8.7262 |
| sortino_ratio | -4.3772 |
| max_drawdown | 0.9950 |
| cagr | -0.8775 |
| net_avg_win | 21.5436 |
| net_avg_loss | -29.5995 |
| avg_hold_time_bars | 4.4130 |
| exposure | 0.2524 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
