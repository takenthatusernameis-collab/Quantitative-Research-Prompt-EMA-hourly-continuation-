# EMA Hourly Continuation — SAFE/USDT P12_100

**Symbol:** SAFE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.8649 |
| net_win_rate | 0.5133 |
| gross_profit_factor | 1.0419 |
| gross_win_rate | 0.5133 |
| sharpe_ratio | -0.9310 |
| sortino_ratio | -0.2850 |
| max_drawdown | 0.3494 |
| cagr | -0.1264 |
| net_avg_win | 78.9641 |
| net_avg_loss | -96.2734 |
| avg_hold_time_bars | 28.0066 |
| exposure | 0.5797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
