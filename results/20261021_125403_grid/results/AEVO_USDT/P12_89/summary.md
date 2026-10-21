# EMA Hourly Continuation — AEVO/USDT P12_89

**Symbol:** AEVO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.8060 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9828 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -1.6816 |
| sortino_ratio | -0.5391 |
| max_drawdown | 0.5225 |
| cagr | -0.2213 |
| net_avg_win | 78.0599 |
| net_avg_loss | -93.8343 |
| avg_hold_time_bars | 24.3360 |
| exposure | 0.5572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
