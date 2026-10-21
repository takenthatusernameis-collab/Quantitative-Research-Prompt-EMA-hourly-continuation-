# EMA Hourly Continuation — CVX/USDT P12_144

**Symbol:** CVX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.7803 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9130 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -1.2915 |
| sortino_ratio | -0.3284 |
| max_drawdown | 0.3429 |
| cagr | -0.1417 |
| net_avg_win | 73.0161 |
| net_avg_loss | -87.9025 |
| avg_hold_time_bars | 48.2062 |
| exposure | 0.7012 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
