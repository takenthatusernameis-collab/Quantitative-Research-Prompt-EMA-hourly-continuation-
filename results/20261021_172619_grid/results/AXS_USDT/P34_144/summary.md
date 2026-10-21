# EMA Hourly Continuation — AXS/USDT P34_144

**Symbol:** AXS/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.8910 |
| net_win_rate | 0.5274 |
| gross_profit_factor | 1.1108 |
| gross_win_rate | 0.5303 |
| sharpe_ratio | -0.6198 |
| sortino_ratio | -0.1660 |
| max_drawdown | 0.2471 |
| cagr | -0.0763 |
| net_avg_win | 81.0152 |
| net_avg_loss | -101.4639 |
| avg_hold_time_bars | 25.8012 |
| exposure | 0.4051 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
