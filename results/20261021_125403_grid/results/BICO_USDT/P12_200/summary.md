# EMA Hourly Continuation — BICO/USDT P12_200

**Symbol:** BICO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.8701 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 1.0002 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -0.7321 |
| sortino_ratio | -0.1817 |
| max_drawdown | 0.2843 |
| cagr | -0.0831 |
| net_avg_win | 86.9022 |
| net_avg_loss | -100.5390 |
| avg_hold_time_bars | 54.1894 |
| exposure | 0.7414 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
