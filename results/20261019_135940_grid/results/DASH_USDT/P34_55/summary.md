# EMA Hourly Continuation — DASH/USDT P34_55

**Symbol:** DASH/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 935 |
| net_profit_factor | 0.3060 |
| net_win_rate | 0.4171 |
| gross_profit_factor | 0.8612 |
| gross_win_rate | 0.4471 |
| sharpe_ratio | -9.5192 |
| sortino_ratio | -4.1144 |
| max_drawdown | 0.9951 |
| cagr | -0.8793 |
| net_avg_win | 11.2521 |
| net_avg_loss | -26.3099 |
| avg_hold_time_bars | 3.1818 |
| exposure | 0.1352 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
