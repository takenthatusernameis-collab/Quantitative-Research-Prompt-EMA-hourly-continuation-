# EMA Hourly Continuation — LUNA/USDT P20_200

**Symbol:** LUNA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.6309 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.9426 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -3.2915 |
| sortino_ratio | -1.0061 |
| max_drawdown | 0.7161 |
| cagr | -0.3827 |
| net_avg_win | 53.5882 |
| net_avg_loss | -76.7185 |
| avg_hold_time_bars | 27.6525 |
| exposure | 0.5933 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
