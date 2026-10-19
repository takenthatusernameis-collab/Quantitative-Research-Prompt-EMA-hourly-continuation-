# EMA Hourly Continuation — IMX/USDT P26_144

**Symbol:** IMX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.7248 |
| net_win_rate | 0.5140 |
| gross_profit_factor | 1.0278 |
| gross_win_rate | 0.5140 |
| sharpe_ratio | -1.8811 |
| sortino_ratio | -0.5702 |
| max_drawdown | 0.5177 |
| cagr | -0.2391 |
| net_avg_win | 54.8810 |
| net_avg_loss | -80.0738 |
| avg_hold_time_bars | 23.9720 |
| exposure | 0.5044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
