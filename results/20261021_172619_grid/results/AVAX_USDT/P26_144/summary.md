# EMA Hourly Continuation — AVAX/USDT P26_144

**Symbol:** AVAX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.8035 |
| net_win_rate | 0.4956 |
| gross_profit_factor | 0.9916 |
| gross_win_rate | 0.4956 |
| sharpe_ratio | -1.3980 |
| sortino_ratio | -0.3688 |
| max_drawdown | 0.4457 |
| cagr | -0.1568 |
| net_avg_win | 84.3109 |
| net_avg_loss | -103.0952 |
| avg_hold_time_bars | 26.8094 |
| exposure | 0.4155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
