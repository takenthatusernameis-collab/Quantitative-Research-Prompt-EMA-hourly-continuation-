# EMA Hourly Continuation — 1INCH/USDT P100_144

**Symbol:** 1INCH/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 239 |
| net_profit_factor | 0.6311 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.9249 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -2.2786 |
| sortino_ratio | -0.5052 |
| max_drawdown | 0.4493 |
| cagr | -0.2067 |
| net_avg_win | 66.1607 |
| net_avg_loss | -95.6150 |
| avg_hold_time_bars | 6.4142 |
| exposure | 0.0697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
