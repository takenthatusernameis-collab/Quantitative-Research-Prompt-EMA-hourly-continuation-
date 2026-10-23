# EMA Hourly Continuation — SAFE/USDT P34_144

**Symbol:** SAFE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.6745 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 0.9894 |
| gross_win_rate | 0.5020 |
| sharpe_ratio | -2.5444 |
| sortino_ratio | -0.7952 |
| max_drawdown | 0.6289 |
| cagr | -0.3174 |
| net_avg_win | 51.9337 |
| net_avg_loss | -76.3721 |
| avg_hold_time_bars | 19.3943 |
| exposure | 0.4370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
