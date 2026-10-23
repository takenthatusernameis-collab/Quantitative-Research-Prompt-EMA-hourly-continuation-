# EMA Hourly Continuation — ALEX/USDT P21_89

**Symbol:** ALEX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 573 |
| net_profit_factor | 0.5851 |
| net_win_rate | 0.4293 |
| gross_profit_factor | 0.8712 |
| gross_win_rate | 0.4328 |
| sharpe_ratio | -5.0314 |
| sortino_ratio | -1.6816 |
| max_drawdown | 0.8832 |
| cagr | -0.5610 |
| net_avg_win | 50.0806 |
| net_avg_loss | -64.3872 |
| avg_hold_time_bars | 17.0419 |
| exposure | 0.4439 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
