# EMA Hourly Continuation — MTL/USDT P8_144

**Symbol:** MTL/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.8541 |
| net_win_rate | 0.5186 |
| gross_profit_factor | 1.0837 |
| gross_win_rate | 0.5186 |
| sharpe_ratio | -0.9253 |
| sortino_ratio | -0.2376 |
| max_drawdown | 0.3634 |
| cagr | -0.1062 |
| net_avg_win | 86.4543 |
| net_avg_loss | -109.0535 |
| avg_hold_time_bars | 54.7143 |
| exposure | 0.7973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
