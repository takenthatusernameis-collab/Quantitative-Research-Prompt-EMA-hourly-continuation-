# EMA Hourly Continuation — DEGEN/USDT P50_89

**Symbol:** DEGEN/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.6075 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.8823 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -4.4096 |
| sortino_ratio | -1.5746 |
| max_drawdown | 0.8479 |
| cagr | -0.5239 |
| net_avg_win | 44.6063 |
| net_avg_loss | -62.7231 |
| avg_hold_time_bars | 5.2469 |
| exposure | 0.1519 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
