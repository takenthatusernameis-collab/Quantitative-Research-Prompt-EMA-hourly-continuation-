# EMA Hourly Continuation — FET/USDT P21_200

**Symbol:** FET/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 1.0077 |
| net_win_rate | 0.5331 |
| gross_profit_factor | 1.1397 |
| gross_win_rate | 0.5331 |
| sharpe_ratio | 0.0847 |
| sortino_ratio | 0.0191 |
| max_drawdown | 0.1416 |
| cagr | 0.0035 |
| net_avg_win | 89.7664 |
| net_avg_loss | -101.6943 |
| avg_hold_time_bars | 63.0413 |
| exposure | 0.6935 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
