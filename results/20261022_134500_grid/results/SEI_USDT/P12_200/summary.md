# EMA Hourly Continuation — SEI/USDT P12_200

**Symbol:** SEI/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.8808 |
| net_win_rate | 0.5472 |
| gross_profit_factor | 1.2355 |
| gross_win_rate | 0.5551 |
| sharpe_ratio | -0.6062 |
| sortino_ratio | -0.1361 |
| max_drawdown | 0.2286 |
| cagr | -0.0657 |
| net_avg_win | 83.4450 |
| net_avg_loss | -114.5065 |
| avg_hold_time_bars | 71.0630 |
| exposure | 0.8205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
