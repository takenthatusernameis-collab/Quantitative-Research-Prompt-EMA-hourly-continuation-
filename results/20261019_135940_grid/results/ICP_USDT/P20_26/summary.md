# EMA Hourly Continuation — ICP/USDT P20_26

**Symbol:** ICP/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1237 |
| net_profit_factor | 0.2195 |
| net_win_rate | 0.3711 |
| gross_profit_factor | 0.7150 |
| gross_win_rate | 0.4188 |
| sharpe_ratio | -14.4088 |
| sortino_ratio | -7.3365 |
| max_drawdown | 1.0000 |
| cagr | -0.9812 |
| net_avg_win | 6.1272 |
| net_avg_loss | -16.4678 |
| avg_hold_time_bars | 1.7421 |
| exposure | 0.0980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
