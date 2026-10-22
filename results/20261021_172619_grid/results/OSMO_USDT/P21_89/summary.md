# EMA Hourly Continuation — OSMO/USDT P21_89

**Symbol:** OSMO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.7721 |
| net_win_rate | 0.4949 |
| gross_profit_factor | 0.9992 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -1.9493 |
| sortino_ratio | -0.6195 |
| max_drawdown | 0.5397 |
| cagr | -0.2481 |
| net_avg_win | 70.9944 |
| net_avg_loss | -90.1060 |
| avg_hold_time_bars | 17.2110 |
| exposure | 0.3857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
