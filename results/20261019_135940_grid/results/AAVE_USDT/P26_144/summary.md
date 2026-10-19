# EMA Hourly Continuation — AAVE/USDT P26_144

**Symbol:** AAVE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.6311 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9467 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -3.2943 |
| sortino_ratio | -1.0284 |
| max_drawdown | 0.7394 |
| cagr | -0.3955 |
| net_avg_win | 50.9363 |
| net_avg_loss | -75.0976 |
| avg_hold_time_bars | 20.2380 |
| exposure | 0.4600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
