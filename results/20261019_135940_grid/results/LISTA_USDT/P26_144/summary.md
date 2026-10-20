# EMA Hourly Continuation — LISTA/USDT P26_144

**Symbol:** LISTA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.6303 |
| net_win_rate | 0.4651 |
| gross_profit_factor | 0.8829 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -3.2258 |
| sortino_ratio | -1.0229 |
| max_drawdown | 0.6806 |
| cagr | -0.3842 |
| net_avg_win | 52.5117 |
| net_avg_loss | -72.4420 |
| avg_hold_time_bars | 19.8710 |
| exposure | 0.4596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
