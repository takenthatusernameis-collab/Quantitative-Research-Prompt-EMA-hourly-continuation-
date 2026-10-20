# EMA Hourly Continuation — ATH/USDT P89_144

**Symbol:** ATH/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.5308 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.8472 |
| gross_win_rate | 0.4639 |
| sharpe_ratio | -4.4746 |
| sortino_ratio | -1.4568 |
| max_drawdown | 0.8130 |
| cagr | -0.5038 |
| net_avg_win | 39.9173 |
| net_avg_loss | -64.0189 |
| avg_hold_time_bars | 4.8795 |
| exposure | 0.1178 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
