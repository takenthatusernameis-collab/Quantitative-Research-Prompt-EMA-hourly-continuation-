# EMA Hourly Continuation — BNB/USDT P12_200

**Symbol:** BNB/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.7662 |
| net_win_rate | 0.5251 |
| gross_profit_factor | 1.0874 |
| gross_win_rate | 0.5251 |
| sharpe_ratio | -1.3163 |
| sortino_ratio | -0.3274 |
| max_drawdown | 0.3364 |
| cagr | -0.1396 |
| net_avg_win | 65.6570 |
| net_avg_loss | -94.7419 |
| avg_hold_time_bars | 52.5585 |
| exposure | 0.7143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
