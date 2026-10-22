# EMA Hourly Continuation — PEPE/USDT P26_144

**Symbol:** PEPE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.6273 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.9140 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -3.4136 |
| sortino_ratio | -1.0527 |
| max_drawdown | 0.7210 |
| cagr | -0.3943 |
| net_avg_win | 53.7991 |
| net_avg_loss | -75.3398 |
| avg_hold_time_bars | 21.8163 |
| exposure | 0.4750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
