# EMA Hourly Continuation — GRAM/USDT P8_144

**Symbol:** GRAM/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.5324 |
| net_win_rate | 0.4621 |
| gross_profit_factor | 0.9179 |
| gross_win_rate | 0.4735 |
| sharpe_ratio | -4.4650 |
| sortino_ratio | -1.4378 |
| max_drawdown | 0.8437 |
| cagr | -0.5060 |
| net_avg_win | 38.7184 |
| net_avg_loss | -62.4839 |
| avg_hold_time_bars | 30.4773 |
| exposure | 0.7315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
