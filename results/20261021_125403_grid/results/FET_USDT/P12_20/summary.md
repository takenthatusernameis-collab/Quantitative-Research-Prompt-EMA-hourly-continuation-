# EMA Hourly Continuation — FET/USDT P12_20

**Symbol:** FET/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 226 |
| net_profit_factor | 0.8768 |
| net_win_rate | 0.5354 |
| gross_profit_factor | 1.1442 |
| gross_win_rate | 0.5354 |
| sharpe_ratio | -0.5901 |
| sortino_ratio | -0.1283 |
| max_drawdown | 0.2204 |
| cagr | -0.0587 |
| net_avg_win | 82.8693 |
| net_avg_loss | -108.9201 |
| avg_hold_time_bars | 5.0088 |
| exposure | 0.0515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
