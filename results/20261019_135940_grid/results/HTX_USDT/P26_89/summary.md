# EMA Hourly Continuation — HTX/USDT P26_89

**Symbol:** HTX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 779 |
| net_profit_factor | 0.3000 |
| net_win_rate | 0.3299 |
| gross_profit_factor | 0.7709 |
| gross_win_rate | 0.3915 |
| sharpe_ratio | -12.0519 |
| sortino_ratio | -4.9163 |
| max_drawdown | 0.9987 |
| cagr | -0.9282 |
| net_avg_win | 16.6552 |
| net_avg_loss | -27.3321 |
| avg_hold_time_bars | 10.2606 |
| exposure | 0.3617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
