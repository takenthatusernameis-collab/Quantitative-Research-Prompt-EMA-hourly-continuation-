# EMA Hourly Continuation — MLK/USDT P50_144

**Symbol:** MLK/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 730 |
| net_profit_factor | 0.2761 |
| net_win_rate | 0.2959 |
| gross_profit_factor | 0.5105 |
| gross_win_rate | 0.3055 |
| sharpe_ratio | -10.7938 |
| sortino_ratio | -4.1514 |
| max_drawdown | 0.9949 |
| cagr | -0.8756 |
| net_avg_win | 17.5697 |
| net_avg_loss | -26.7372 |
| avg_hold_time_bars | 8.1493 |
| exposure | 0.2692 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
