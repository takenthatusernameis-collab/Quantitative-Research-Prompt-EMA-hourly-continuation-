# EMA Hourly Continuation — BOME/USDT P21_144

**Symbol:** BOME/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.6745 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9104 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -2.3220 |
| sortino_ratio | -0.7000 |
| max_drawdown | 0.5956 |
| cagr | -0.2831 |
| net_avg_win | 53.1269 |
| net_avg_loss | -73.4433 |
| avg_hold_time_bars | 26.6463 |
| exposure | 0.5547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
