# EMA Hourly Continuation — CETUS/USDT P12_89

**Symbol:** CETUS/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.9009 |
| net_win_rate | 0.5209 |
| gross_profit_factor | 1.0861 |
| gross_win_rate | 0.5209 |
| sharpe_ratio | -0.7633 |
| sortino_ratio | -0.2512 |
| max_drawdown | 0.3556 |
| cagr | -0.1142 |
| net_avg_win | 87.4609 |
| net_avg_loss | -105.5539 |
| avg_hold_time_bars | 23.0951 |
| exposure | 0.5497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
