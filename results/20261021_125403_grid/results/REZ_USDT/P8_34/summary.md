# EMA Hourly Continuation — REZ/USDT P8_34

**Symbol:** REZ/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 776 |
| net_profit_factor | 0.8210 |
| net_win_rate | 0.5026 |
| gross_profit_factor | 1.0269 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -2.0225 |
| sortino_ratio | -0.8129 |
| max_drawdown | 0.6436 |
| cagr | -0.3140 |
| net_avg_win | 71.2880 |
| net_avg_loss | -87.7353 |
| avg_hold_time_bars | 9.0039 |
| exposure | 0.3224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
