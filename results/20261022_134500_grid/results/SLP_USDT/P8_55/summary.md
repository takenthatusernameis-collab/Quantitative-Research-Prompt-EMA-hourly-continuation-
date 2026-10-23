# EMA Hourly Continuation — SLP/USDT P8_55

**Symbol:** SLP/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1171 |
| net_profit_factor | 0.5802 |
| net_win_rate | 0.4372 |
| gross_profit_factor | 0.8912 |
| gross_win_rate | 0.4500 |
| sharpe_ratio | -7.3190 |
| sortino_ratio | -3.5183 |
| max_drawdown | 0.9870 |
| cagr | -0.8199 |
| net_avg_win | 26.6346 |
| net_avg_loss | -35.6630 |
| avg_hold_time_bars | 9.0273 |
| exposure | 0.4805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
