# EMA Hourly Continuation — DASH/USDT P20_26

**Symbol:** DASH/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1241 |
| net_profit_factor | 0.1344 |
| net_win_rate | 0.3505 |
| gross_profit_factor | 0.6253 |
| gross_win_rate | 0.4021 |
| sharpe_ratio | -15.2984 |
| sortino_ratio | -7.8635 |
| max_drawdown | 1.0000 |
| cagr | -0.9861 |
| net_avg_win | 3.5693 |
| net_avg_loss | -14.3330 |
| avg_hold_time_bars | 1.9033 |
| exposure | 0.1074 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
