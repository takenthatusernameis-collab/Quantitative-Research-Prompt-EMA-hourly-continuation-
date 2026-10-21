# EMA Hourly Continuation — WIN/USDT P144_200

**Symbol:** WIN/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 178 |
| net_profit_factor | 0.4746 |
| net_win_rate | 0.4382 |
| gross_profit_factor | 0.7324 |
| gross_win_rate | 0.4382 |
| sharpe_ratio | -2.7633 |
| sortino_ratio | -0.5288 |
| max_drawdown | 0.4891 |
| cagr | -0.2161 |
| net_avg_win | 52.9733 |
| net_avg_loss | -87.0540 |
| avg_hold_time_bars | 9.0337 |
| exposure | 0.0731 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
