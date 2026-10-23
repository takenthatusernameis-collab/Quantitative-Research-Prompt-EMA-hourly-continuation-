# EMA Hourly Continuation — REZ/USDT P21_200

**Symbol:** REZ/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.8939 |
| net_win_rate | 0.5268 |
| gross_profit_factor | 1.1211 |
| gross_win_rate | 0.5293 |
| sharpe_ratio | -0.7207 |
| sortino_ratio | -0.2104 |
| max_drawdown | 0.3105 |
| cagr | -0.0976 |
| net_avg_win | 87.5237 |
| net_avg_loss | -109.0177 |
| avg_hold_time_bars | 31.9829 |
| exposure | 0.6050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
