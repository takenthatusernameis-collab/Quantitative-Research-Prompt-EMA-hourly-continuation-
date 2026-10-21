# EMA Hourly Continuation — INJ/USDT P12_144

**Symbol:** INJ/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.7475 |
| net_win_rate | 0.4640 |
| gross_profit_factor | 0.8707 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -1.7312 |
| sortino_ratio | -0.4577 |
| max_drawdown | 0.4186 |
| cagr | -0.1904 |
| net_avg_win | 75.7044 |
| net_avg_loss | -87.6650 |
| avg_hold_time_bars | 43.6945 |
| exposure | 0.6892 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
