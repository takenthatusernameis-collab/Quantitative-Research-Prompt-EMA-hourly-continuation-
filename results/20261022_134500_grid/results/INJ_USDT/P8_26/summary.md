# EMA Hourly Continuation — INJ/USDT P8_26

**Symbol:** INJ/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1591 |
| net_profit_factor | 0.5073 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.8846 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -9.0673 |
| sortino_ratio | -5.0600 |
| max_drawdown | 0.9982 |
| cagr | -0.9195 |
| net_avg_win | 14.1201 |
| net_avg_loss | -23.4780 |
| avg_hold_time_bars | 3.6109 |
| exposure | 0.2611 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
