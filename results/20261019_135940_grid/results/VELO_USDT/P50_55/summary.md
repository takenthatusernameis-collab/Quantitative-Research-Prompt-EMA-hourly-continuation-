# EMA Hourly Continuation — VELO/USDT P50_55

**Symbol:** VELO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 830 |
| net_profit_factor | 0.2941 |
| net_win_rate | 0.3675 |
| gross_profit_factor | 0.6978 |
| gross_win_rate | 0.3952 |
| sharpe_ratio | -11.3441 |
| sortino_ratio | -4.7180 |
| max_drawdown | 0.9981 |
| cagr | -0.9169 |
| net_avg_win | 13.6359 |
| net_avg_loss | -26.9326 |
| avg_hold_time_bars | 2.1687 |
| exposure | 0.0818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
