# EMA Hourly Continuation — CETUS/USDT P21_144

**Symbol:** CETUS/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.8168 |
| net_win_rate | 0.5212 |
| gross_profit_factor | 1.1280 |
| gross_win_rate | 0.5232 |
| sharpe_ratio | -1.7008 |
| sortino_ratio | -0.5322 |
| max_drawdown | 0.5790 |
| cagr | -0.2270 |
| net_avg_win | 82.5659 |
| net_avg_loss | -110.0373 |
| avg_hold_time_bars | 23.8162 |
| exposure | 0.5335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
