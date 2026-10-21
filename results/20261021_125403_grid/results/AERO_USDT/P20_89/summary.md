# EMA Hourly Continuation — AERO/USDT P20_89

**Symbol:** AERO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.9011 |
| net_win_rate | 0.5176 |
| gross_profit_factor | 1.0698 |
| gross_win_rate | 0.5176 |
| sharpe_ratio | -0.6938 |
| sortino_ratio | -0.2126 |
| max_drawdown | 0.3373 |
| cagr | -0.0974 |
| net_avg_win | 87.9602 |
| net_avg_loss | -104.7465 |
| avg_hold_time_bars | 17.2467 |
| exposure | 0.3559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
