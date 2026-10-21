# EMA Hourly Continuation — ENJ/USDT P8_55

**Symbol:** ENJ/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 712 |
| net_profit_factor | 0.8038 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 1.0218 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -1.8994 |
| sortino_ratio | -0.7241 |
| max_drawdown | 0.5988 |
| cagr | -0.2848 |
| net_avg_win | 65.1356 |
| net_avg_loss | -82.4112 |
| avg_hold_time_bars | 13.8890 |
| exposure | 0.4475 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
